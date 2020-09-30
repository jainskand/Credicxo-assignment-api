from rest_framework import permissions

#permission class to allow only teacher or superadmin to access get or post methods
class IsTeacherOrSuperAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        # if user is django-admin then allowed to access
        if request.user.is_staff:
            return True
        #checking if user.groups having teacher or superadmin
        groups = [group.name for group in request.user.groups.all()]
        return  len(set(groups)&set(('teacher','superadmin')))!=0

#permission class to allow only superadmin to access get or post methods
class IsSuperAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        # if user is django-admin then allowed to access
        if request.user.is_staff:
            return True
        #checking if user.groups having superadmin or not
        groups = [group.name for group in request.user.groups.all()]
        return  len(set(groups)&set(('superadmin',)))!=0
