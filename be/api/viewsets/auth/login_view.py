from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import User
from api.utils.jwt import generate_token
# from api.utils.hit_api import get_ithc_employee_info, get_user_detail, login_eai
from api.exceptions import InvalidCredentialException, NotEligibleException, NotAuthenticatedException, ValidationException
# from api.utils.enum import RoleEnum
from cryptography.fernet import Fernet
from ...models import User
from django.conf import settings
from api.utils.pycrypto import encrypt_data,decrypt_data

class LoginView(APIView):
    def post(self, request):
        if "username" not in request.data:
            return Response({'message': 'username must be filled'})
        if "password" not in request.data:
            return Response({'message': 'password must be filled'})
        
        username = request.data['username']
        password = request.data['password']

        try:
            login_user = User.objects.get(username=username)
            # fernet = Fernet(settings.FERNET_KEY)
            # password_db = fernet.decrypt(bytes(login_user.password.encode()))
            # password_request = fernet.decrypt(bytes(password.encode()))
            password_request = decrypt_data(password).decode("utf-8", "ignore")
            password_db = decrypt_data(login_user.password).decode("utf-8", "ignore")
            if password_db != password_request:
                raise InvalidCredentialException()
        except:
            raise InvalidCredentialException()
        
        jwt = generate_token(login_user.id, login_user.username, login_user.name, login_user.role.name)

        response = Response({
            'id':login_user.id,
            'username': login_user.username,
            'name': login_user.name,
            'role': login_user.role.name
        })

        response.set_cookie(
            key='Bte8wiZdhuuwmItf0lioiEfe9oPh9ArBi_lHlUZQI50',
            value=jwt,
            httponly=True,
            # domain="localhost"
            # samesite='None',
            # secure=True   
        )
                
        return response