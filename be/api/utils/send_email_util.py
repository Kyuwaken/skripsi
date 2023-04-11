import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from ..models import Transaction
from ..serializers import TransactionResponseNotificationSerializer
from email.message import EmailMessage
from django.template.loader import render_to_string

from rest_framework.response import Response
from rest_framework import status
import json, copy
import locale, datetime

def rupiah_format(angka, with_prefix=True, desimal=2):
    locale.setlocale(locale.LC_NUMERIC, 'IND')
    rupiah = locale.format("%.*f", (desimal, angka), True)
    if with_prefix:
        return "Rp {}".format(rupiah)
    return rupiah

# username='u067648@dti.co.id'
username='gsit_panda@bca.co.id'
password=''

# username='edummy12345@gmail.com'
# password='123dummy456'

EMAIL_ADDRESS = "testingspider0@gmail.com"
EMAIL_PASSWORD = "#Admin123"
EMAIL_BCA = 'u067648@dti.co.id,u06764812@dti.co.id'
# EMAIL_BCA = 'yosefina_santoso@dti.co.id'
def send_mail(text,subject,to_emails):
    assert isinstance(to_emails,list)
    # mengatur bentuk message
    msg=MIMEMultipart('alternative')
    msg['From']=username
    msg['To']=", ".join(to_emails)
    msg['Subject']=subject
    txt_part=MIMEText(text,'plain')
    msg.attach(txt_part)
    html_part = MIMEText(f"<p>{text}</p>", 'html')
    msg.attach(html_part)
    msg_str=msg.as_string()
    # connect ke server
    # server=smtplib.SMTP(host='10.27.2.126' ,port='25')
    server=smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    # login
    server.login(username,password)
    # send email
    server.sendmail(username,to_emails,msg_str)
    server.quit()

    return({
        'from': str(msg['From']),
        'to': str(msg['To']),
        'subject': str(msg['Subject']),
        'text': str(text)
    })

def already_pay_dp(data):
    products = data['transaction_detail']
    
    seller = products[0]['transaction']['seller']
    customer = products[0]['transaction']['customer']
    seller_email= products[0]['transaction']['seller']['email']
    customer_email = products[0]['transaction']['customer']['email']
    payload = []
    total = 0
    for i in products:
        container = {}
        container['name'] = i['product']['name']
        container['price'] = rupiah_format(i['product']['price'])
        container['quantity'] = i['quantity']
        container['sub_total'] = rupiah_format(i['total'])
        total += i['total']
        payload.append(container)
    # breakpoint()
    
    return payload, seller, customer, rupiah_format(total), 
    


def send_notification(subject,tr_id,type):
    
    # msg=MIMEMultipart('alternative')
    # msg['From']=username
    # msg['To']=send_to
    # msg['Subject']=subject
    # txt_part=MIMEText(body,'plain')
    # msg.attach(txt_part)
    # html_part = MIMEText(f"<p>{body}</p>", 'html')
    # msg.attach(html_part)
    # msg_str=msg.as_string()

    # ambil dr templates bentuk messagenya untuk bikin data karyawan bentuk table
    dict_type = {
        'already_pay_dp':'notification_already_pay_dp.html', #to customer
        'product_to_be_confirm':'notification_product_to_be_confirm.html', #to seller
        'confirmation_product':'notification_confirmation_product.html', #to customer that seller accept transaction
        'seller_buy_product':'notification_seller_buy_product.html', #to seller need to buy the product before the pre order
        'seller_reject_transaction':'notification_seller_reject_transaction.html', #to customer
        'to_full_payment':'notification_to_full_payment.html', #to customer
        'time_limit_confirmation': 'notification_time_limit_confirmation.html', #to customer and seller
        'time_limit_preorder': 'notification_time_limit_preorder.html', #to customer and seller
        'time_limit_full_payment': 'notification_time_limit_payment.html', #to customer and seller
        'time_limit_send_product':'notification_time_limit_send_product.html', #to customer and seller
        'product_need_to_send': 'notification_product_need_to_send.html', #to seller send the product that already fp by customer
        'already_pay_fp':'notification_already_pay_fp.html', #to customer
        'sending_product': 'notification_sending_product.html', #to_customer
        'product_delivered': 'notification_product_delivered.html', #to customer and seller
        'complain_delivering':'notification_complain_delivering.html' #to admin
    }
    # breakpoint()
    msg = EmailMessage()
    msg['X-Priority'] = '2'
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    transaction = Transaction.objects.get(pk=tr_id)
    serz = TransactionResponseNotificationSerializer(transaction,many=False)
    data = copy.deepcopy(serz.data)
    body, seller, customer, total  = already_pay_dp(data)
    if type in ['already_pay_dp','product_to_be_confirm']:
        if type == 'already_pay_dp':
            msg['To'] = customer['email']
        else:
            msg['To'] = seller['email']
        for i in data['payment']:
            if i['paymentType']['name'] == 'Down Payment':
                dp = rupiah_format(i['nominal'])
        for i in data['transaction_status']:
            if i['masterStatus']['id'] == 1:
                time_limit = ((datetime.datetime.strptime(i['dateOrdered'],'%Y-%m-%dT%H:%M:%S.%f%z')).date() + datetime.timedelta(days=3)).strftime('%d %B %Y')
        message = render_to_string(dict_type[type],{'body': body,'seller':seller,'customer':customer,'total':total,'dp':dp,'timelimit':time_limit})
    
    if type == 'confirmation_product':
        msg['To'] = customer['email']
        for i in data['transaction_status']:
            if i['masterStatus']['id'] == 2:
                time_limit = ((datetime.datetime.strptime(i['dateOrdered'],'%Y-%m-%dT%H:%M:%S.%f%z')).date() + datetime.timedelta(days=data['preOrderTime'])).strftime('%d %B %Y')
        message = render_to_string(dict_type[type],{'body': body,'seller':seller,'customer':customer,'total':total,'timelimit':time_limit})

    if type == 'seller_buy_product':
        msg['To'] = seller['email']
        for i in data['transaction_status']:
            if i['masterStatus']['id'] == 2:
                time_limit = ((datetime.datetime.strptime(i['dateOrdered'],'%Y-%m-%dT%H:%M:%S.%f%z')).date() + datetime.timedelta(days=data['preOrderTime'])).strftime('%d %B %Y')
        message = render_to_string(dict_type[type],{'body': body,'seller':seller,'customer':customer,'total':total,'timelimit':time_limit})
    if type == 'seller_reject_transaction':
        pass
    
    if type == 'to_full_payment':
        msg['To'] = customer['email']
        for i in data['payment']:
            if i['paymentType']['name'] == 'Down Payment':
                dp = rupiah_format(i['nominal'])
            if i['paymentType']['name'] == 'Full Payment':
                fp = rupiah_format(i['nominal'])
        for i in data['transaction_status']:
            if i['masterStatus']['id'] == 3:
                time_limit = ((datetime.datetime.strptime(i['dateOrdered'],'%Y-%m-%dT%H:%M:%S.%f%z')).date() + datetime.timedelta(days=3)).strftime('%d %B %Y')
        message = render_to_string(dict_type[type],{'body': body,'seller':seller,'customer':customer,'total':total,'fp':fp,'dp':dp,'timelimit':time_limit})
    
    if type == 'time_limit_confirmation':
        pass

    if type == 'time_limit_preorder':
        pass

    if type == 'time_limit_full_payment':
        pass

    if type == 'time_limit_send_product':
        pass

    if type == 'already_pay_fp':
        msg['To'] = customer['email']
        for i in data['payment']:
            if i['paymentType']['name'] == 'Full Payment':
                fp = rupiah_format(i['nominal'])
        for i in data['transaction_status']:
            if i['masterStatus']['id'] == 4:
                time_limit = ((datetime.datetime.strptime(i['dateOrdered'],'%Y-%m-%dT%H:%M:%S.%f%z')).date() + datetime.timedelta(days=3)).strftime('%d %B %Y')
        message = render_to_string(dict_type[type],{'body': body,'seller':seller,'customer':customer,'total':total,'fp':fp,'timelimit':time_limit})

    if type == 'product_need_to_send':
        msg['To'] = seller['email']
        address = data['address']
        for i in data['transaction_status']:
            if i['masterStatus']['id'] == 4:
                time_limit = ((datetime.datetime.strptime(i['dateOrdered'],'%Y-%m-%dT%H:%M:%S.%f%z')).date() + datetime.timedelta(days=3)).strftime('%d %B %Y')
        message = render_to_string(dict_type[type],{'body': body,'seller':seller,'customer':customer,'total':total,'timelimit':time_limit,'address':address})
    
    if type == 'sending_product':
        msg['To'] = customer['email']
        
    if type == 'product_delivered':
        pass

    
    
    # #masukkan ke msg set content
    msg.set_content(message, subtype='html')
    
    # To_list = [x.strip() for x in send_to.split(',')]  #bentuk to harus dalam list dibawah To = ['yosefina_santoso@bca.co.id', 'andrew_ciayandi@bca.co.id']
    
    #sambungkan ke smtp email
    # try:
    #     server=smtplib.SMTP(host='10.22.64.10' ,port='25')
    #     server.ehlo()
    #     server.sendmail(username,To_list,msg_str)
    #     server.quit()
    # except:
    #     try:    
    #         server=smtplib.SMTP(host='10.6.64.10' ,port='25')
    #         server.ehlo()
    #         server.sendmail(username,To_list,msg_str)
    #         server.quit()    
    #     except:
    #         try:
    #             server=smtplib.SMTP(host='10.38.64.10' ,port='25')
    #             server.ehlo()
    #             server.sendmail(username,To_list,msg_str)
    #             server.quit()  
    #         except:  
    #             return ({"Status" :"Failed"})
    # server=smtplib.SMTP(host='smtp.gmail.com' ,port='465')
    # server.ehlo()
    # server.starttls()
    # server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    # server.sendmail(EMAIL_ADDRESS,To,msg_str)
    # server.quit()
    #sambungkan ke smtp email
    try:
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.starttls()
            smtp.login("vincentchris012@gmail.com", "frnobdncrvtcmnci")
            # smtp.sendmail("vincentchris012@gmail.com",msg['To'],msg)
            # smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
            smtp.quit()
        # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server.ehlo()
        # server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        # server.sendmail(EMAIL_ADDRESS, msg['To'], msg)
        # server.close()
    except:
        return ({"Status" :"Failed"})
    # try:
    #     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #         smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    #         smtp.sendmail(EMAIL_ADDRESS,send_to,msg)
    #         smtp.quit()
    #         # smtp.send_message(msg)
    # except:
    #     return ({"Status" :"Failed"})
    # untuk print response dengan email siapa saja yang success
    # successSend=successSend + ', '  + manager.display_name+"("+manager.work_email+")" + ', ' 

    
    return ({
        "Status" :"Succeed"
    })
