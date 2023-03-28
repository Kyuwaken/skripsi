import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from ..models import Biro,SubGroup,Group , Employee,PicMPP
from email.message import EmailMessage
from django.template.loader import render_to_string

from rest_framework.response import Response
from rest_framework import status
import json

# username='u067648@dti.co.id'
username='gsit_panda@bca.co.id'
password=''

# username='edummy12345@gmail.com'
# password='123dummy456'

EMAIL_ADDRESS = "edummy12345@gmail.com"
EMAIL_PASSWORD = "123dummy456"
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

def send_notification(subject,body,send_to):
    
    msg=MIMEMultipart('alternative')
    msg['From']=username
    msg['To']=send_to
    msg['Subject']=subject
    txt_part=MIMEText(body,'plain')
    msg.attach(txt_part)
    html_part = MIMEText(f"<p>{body}</p>", 'html')
    msg.attach(html_part)
    msg_str=msg.as_string()

    # ambil dr templates bentuk messagenya untuk bikin data karyawan bentuk table
    # message = render_to_string('email_format.html',{ 'body': body})
    # #masukkan ke msg set content
    # msg.set_content(message, subtype='html')
    
    To_list = [x.strip() for x in send_to.split(',')]  #bentuk to harus dalam list dibawah To = ['yosefina_santoso@bca.co.id', 'andrew_ciayandi@bca.co.id']
    
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
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.sendmail(EMAIL_ADDRESS,send_to,msg)
            smtp.quit()
            # smtp.send_message(msg)
    except:
        return ({"Status" :"Failed"})
    # untuk print response dengan email siapa saja yang success
    # successSend=successSend + ', '  + manager.display_name+"("+manager.work_email+")" + ', ' 

    
    return ({
        "Status" :"Succeed"
    })
