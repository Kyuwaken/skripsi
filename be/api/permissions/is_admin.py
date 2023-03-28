from rest_framework import permissions

from api.exceptions import NotAuthorizedException


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.custom_user and request.custom_user['role'] == "Admin":
            return True
        raise NotAuthorizedException()
