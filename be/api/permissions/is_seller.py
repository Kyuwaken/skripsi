from rest_framework import permissions

from api.exceptions import NotAuthorizedException


class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.custom_user and request.custom_user['role'] == "Seller":
            return True
        raise NotAuthorizedException()
