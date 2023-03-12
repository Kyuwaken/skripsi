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

def is_manager(user):
    return user['biro_manager_id'] == user['employee_id'] or user['sub_group_manager_id'] == user['employee_id'] or user['group_manager_id'] == user['employee_id']

def get_admin(username):
    #Check if admin exists in Budgetin DB
    # breakpoint()
    admin = User.objects.filter(username__iexact=username, role=RoleEnum.ADMIN.value).first()
    if admin:
        if not admin.is_deleted and admin.is_active:
            try:
                display_name, initial, eselon, ithc_biro, group, subgroup = get_user_detail(username)
                return {
                    'display_name': display_name,
                    'role': RoleEnum.ADMIN.value,
                    'initial': initial if initial else '-',
                    'eselon': eselon,
                    'ithc_biro': ithc_biro,
                    'group': group,
                    'subgroup': subgroup
                }
            except:
                raise ValidationException('Error while get employee api')
    raise NotEligibleException()

def get_user(username):
    #Check if User is S1, S2, S3 in DB
    user = get_ithc_employee_info(username)
    if is_manager(user):
        return {
                'display_name': user['display_name'],
                'role': RoleEnum.USER.value,
                'initial': user['initial'] if user['initial'] else '-',
                'eselon': user['eselon'],
                'ithc_biro': user['biro_id'],
                'group': user['group_code'],
                'subgroup': user['sub_group_code']
            }
    raise NotEligibleException()

def get_user_info(username, user_role):
    
    if user_role.lower() == RoleEnum.ADMIN.value.lower():
        return get_admin(username)
    elif user_role.lower() == RoleEnum.USER.value.lower():
        return get_user(username)

class LoginView(APIView):
    def post(self, request):
        if "username" not in request.data:
            return Response({'message': 'username must be filled'})
        if "password" not in request.data:
            return Response({'message': 'password must be filled'})
        if "role" not in request.data:
            return Response({'message': 'role must be filled'})
        # breakpoint()
        username = request.data['username']
        user_role = request.data['role']
        password = request.data['password'] #delete if use fernet
        # breakpoint()
        try:
            login_user = User.objects.get(username=username,role__name = user_role,password=password)
        except:
            raise InvalidCredentialException()

        # Check if users exists in Budgetin/ITHC database
        
        # user_info = get_user_info(username, user_role)

        # Decrypt password
        # fernet = Fernet(settings.FERNET_KEY)
        # password = fernet.decrypt(request.data['password'].encode()).decode()
        # print(password)
        # Hit EAI
        # eai_login_status = login_eai(username, password)
        # eai_login_status = "Berhasil" #DEBT
        # If EAI success, Get ITHC EmployeeID
        # if eai_login_status != "Berhasil" and password != settings.PASSWORDITF:
            # raise InvalidCredentialException()
        
        # If user with given username & employee_id exists, update display_name, initial and eselon
        # Else create new user with given username, employee_id and display_name, initial and eselon 
        # user, created = User.objects.update_or_create(
            # username=username,
            # defaults={'display_name': user_info['display_name']}
        # )
        # user = {}
        # try:
        #     user = User.objects.get(username=username,employee_id = user_info['employee_id'])
        #     user.display_name = user_info['display_name']
        #     user.initial = user_info['initial']
        #     user.eselon = user_info['eselon']
        # except:
        #     user['id'] = None
        # Generate jwt
        # if user_role.lower() == RoleEnum.USER.value.lower():
        jwt = generate_token(login_user.id, login_user.username, login_user.name, login_user.role.name)
        # else:
        #     jwt = generate_token(user.id, username, user_info['display_name'], user_info['role'], user_info['eselon'], user_info['initial'], user_info['ithc_biro'])
        response = Response({
            'username': username,
            'display_name': login_user.name,
            'role': login_user.role.name
        })
        response.set_cookie(
            key='Bte8wiZdhuuwmItf0lioiEfe9oPh9ArBi_lHlUZQI50',
            value=jwt,
            httponly=True,
            # domain='localhost'
            # domain="localhost"
            # samesite='None',
            # secure=True   
        )
                
        return response