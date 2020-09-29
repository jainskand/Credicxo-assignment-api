from rest_framework import permissions


class IsTeacherOrSuperAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        groups = [group.name for group in request.user.groups.all()]
        return  len(set(groups)&set(('teacher','supeadmin')))!=0


class IsSuperAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        groups = [group.name for group in request.user.groups.all()]
        return  len(set(groups)&set(('supeadmin')))!=0
