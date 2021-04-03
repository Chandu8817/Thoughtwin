from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, userobj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return userobj.user == request.user