from rest_framework import permissions


class IsTeacherOrSuperAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        groups = [group.name for group in request.user.groups.all()]
        return  len(set(groups)&set(('teacher','superadmin')))!=0


class IsSuperAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        groups = [group.name for group in request.user.groups.all()]
        return  len(set(groups)&set(('superadmin',)))!=0
