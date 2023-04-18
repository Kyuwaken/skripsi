from rest_framework import permissions

from api.exceptions import NotAuthorizedException


class IsSignUp(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True        
        if hasattr(request, 'custom_user'):
            return True
        raise NotAuthorizedException()
