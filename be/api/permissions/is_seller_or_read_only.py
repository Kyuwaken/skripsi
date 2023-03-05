from rest_framework import permissions

from api.exceptions import NotAuthorizedException


class IsSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method == 'DELETE' and request.custom_user and request.custom_user['role'] == 'Admin':
            return True
        if request.custom_user and request.custom_user['role'] == "Seller":
            return True
        raise NotAuthorizedException()
