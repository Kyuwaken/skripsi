from api.models import RequestLog
from api.utils.triple_des import TripleDES
import json
from django.conf import settings
from api.middleware.custom_get_current_middleware import *


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # role = None
        # if get_current_user()!='AnonymousUser':
        #     userDetail = User.objects.get(username=get_current_user())
        #     if userDetail.is_staff:
        #         if userDetail.is_unitKerja:
        #             role = RequestLog.ADMIN
        #         else:
        #             role = RequestLog.ITHC
        #     elif userDetail.is_unitKerja:
        #         role = RequestLog.UNITKERJA
        user = get_current_user()
        data = {
            'user': user['id'] if user else None,
            'url': request.path,
            'method': request.method,
            'parameter': json.dumps(request.GET),
            'header': json.dumps(dict(request.headers)),
            'body': "{}",
            'response_code': 0,
            'role': user['role'] if user else None
        }

        request_log = RequestLog(**data)
        request_log.save()
        set_current_request_log(request_log)

        response = self.get_response(request)

        if request.content_type == "application/json":

            body = json.loads(request.body)
            try:
                if (body["password"] != None):
                    # chipper = encrypt_3des(ENV_VARIABLE['KEY_ID'])
                    chipper = TripleDES('AdiNIad19624KG6RI5838hda')
                    encrypted_pass = chipper.encrypt(body["password"])
                    # encrypted_pass = "'''" + encrypt_3des(body["password"], settings.EAI_PUBLIC_KEY) + "'''"
                    body["password"] = encrypted_pass
            except:
                pass
            body = json.dumps(body)

        else:
            try:
                if (request.POST["password"] != None):
                    # chipper = TripleDES(ENV_VARIABLE['KEY_ID'])
                    chipper = TripleDES('AdiNIad19624KG6RI5838hda')
                    encrypted_pass = chipper.encrypt(body["password"])
                    # encrypted_pass = "'''" + encrypt_3des(request.POST["password"], settings.EAI_PUBLIC_KEY) + "'''"
                    request.POST._mutable = True
                    request.POST["password"] = encrypted_pass
                    request.POST._mutable = False
            except:
                pass
            body = json.dumps(request.POST)

        request_log.response_code = response.status_code
        request_log.body = body
        request_log.save()

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        getattr(request, '_body', request.body)
        return None


