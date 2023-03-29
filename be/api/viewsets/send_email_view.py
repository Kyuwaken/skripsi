from ..utils import send_mail, send_notification, sendApproval
from rest_framework.response import Response
import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import json
from rest_framework import status
from ..models import Notif
from custom_viewset.models import  Log
from custom_viewset.utils.generate import generate_structure
from custom_viewset import get_current_user
from custom_viewset.utils.serialize import Serializer
from django.core.serializers.json import DjangoJSONEncoder

class SendNotificationViewSet(APIView):

    def writeHistory(self,user,instance,data):
        log = Log(
            user=user,
            object_id=instance.id,
            serialized_data=json.dumps(data, cls=DjangoJSONEncoder),
            object_repr=str(instance),
            content_type=Log().get_content_type(instance),
            action=Log.UPDATED
        )
        log.save()   


    def post(self, request):
        reqbody=json.loads(request.body)
        subject = reqbody['subject']
        body = reqbody['body']
        send_to = reqbody["send_to"]
        notif_id= reqbody["id"]
        instance = Notif.objects.get(pk = notif_id)
        # breakpoint()
        sending = send_notification(subject,body,send_to)
        full = [{
            "field": "Mail" ,
            "Status" : "Success" if sending["Status"] != "Failed" else "Failed", 
            "Sent to" : send_to , 
            "Subject": subject , 
            "Body": body , 
            "Detail send to" : sending["Email_Sended"] if "Email_Sended" in sending else "None",
            "Kabiro Sent" :  sending["Kabiro_Sended"] if "Kabiro_Sended" in sending else "None"
            }]
        if sending["Status"] == "Failed" : 
            full.append({"Reason" : "Failed in sending, Fail to Connect to SMTP server"}) 
        self.writeHistory(request.user.display_name, instance,full)

        return Response(sending, status=200) if sending["Status"] != "Failed" else Response({"Status" :"Failed in sending, Fail to Connect to SMTP server"}, status.HTTP_400_BAD_REQUEST)

    # @action(detail=False, methods=['post'])
    # def takeOverRequest(self,request,*args,**kwargs):
    #     reqbody=json.loads(request.body)

    #     subject = reqbody['subject']
    #     body = reqbody['body']
    #     send_to = reqbody["send_to"]

    #     sending = sendApproval(subject,body,send_to)



