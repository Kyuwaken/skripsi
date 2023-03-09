from api.utils.jwt import decode_token
from django.conf import settings
from api.middleware.custom_get_current_middleware import set_current_user
from rest_framework.response import Response
from rest_framework import status

class CustomAuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def process_request(self, request):
        # breakpoint()
        token = request.COOKIES.get('token')
        if token:
            user = decode_token(token)
            if user:
                request.custom_user = user
                # untuk log
                set_current_user(user)
        # else: #DEBT. delete this else block
        #     request.custom_user = {
        #         "id": 4,
        #         "username": "u05217",
        #         "display_name": "Winoto Sugiarto",
        #         "role": "User",
        #         "eselon": "S3",
        #         "initial": "WIN",
        #         "ithc_biro": 37
        #     }
                
        return None
