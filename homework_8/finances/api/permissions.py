from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    message = 'Not found.'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsChargeOwner(BasePermission):
    message = 'Not found.'

    def has_object_permission(self, request, view, obj):
        return obj.account.user == request.user
