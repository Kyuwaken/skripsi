from api.utils.jwt import decode_token
from django.conf import settings
from api.middleware.custom_get_current_middleware import set_current_user
from rest_framework.response import Response
from rest_framework import status
from re import sub
from rest_framework.authentication import get_authorization_header
from api.utils.pycrypto import decrypt_data_fe
from ..models import User

class CustomAuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def process_request(self, request):
        # breakpoint()
        # token = request.COOKIES.get('Bte8wiZdhuuwmItf0lioiEfe9oPh9ArBi_lHlUZQI50')
        # if token:
        #     user = decode_token(token)
        #     if user:
        #         request.custom_user = user
        #         # untuk log
        #         set_current_user(user)
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
        header_token = request.META.get('HTTP_AUTHORIZATION', None)
        if header_token is not None:
            token = sub('Token ', '', request.META.get('HTTP_AUTHORIZATION', None))
            # auth = get_authorization_header(request).split()
            # token = decode_token(auth[1].decode())
            # breakpoint()
            data = decrypt_data_fe(token)
            request.custom_user = data
            set_current_user = data
            # user = User.objects.get(pk=data)
            # user_data = {"id":user.id,"name":user.name,"username":user.username,'role':user.role}
            # request.custom_user = user_data
            # set_current_user(user_data)

        return None
