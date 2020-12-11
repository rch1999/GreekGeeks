from rest_framework import permissions


class IsOrganizationAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not(request.user and request.user.is_authenticated):
            return False

        orgId = obj['orgId']
        user = request.user
        is_admin = user.admin_of.filter(uuid=orgId).count() > 0
        return is_admin


class IsOrganizationMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not(request.user and request.user.is_authenticated):
            return False

        orgId = obj['orgId']
        user = request.user
        is_member = user.member_of.filter(uuid=orgId).count() > 0
        return is_member


class IsOrganizationAdminOrReadOnly(permissions.BasePermission):
    SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

    def has_object_permission(self, request, view, obj):
        if not(request.user and request.user.is_authenticated):
            return False

        orgId = obj['orgId']
        user = request.user
        is_member = user.member_of.filter(uuid=orgId).count() > 0
        is_admin = user.admin_of.filter(uuid=orgId).count() > 0

        return (is_member and request.method in IsOrganizationAdminOrReadOnly.SAFE_METHODS) or is_admin


class IsOrganizationAdminOrPostOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not(request.user and request.user.is_authenticated):
            return False

        orgId = obj['orgId']
        user = request.user
        is_admin = user.admin_of.filter(uuid=orgId).count() > 0

        return is_admin or request.method == 'POST'


class OwnsAccount(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not(request.user and request.user.is_authenticated):
            return False

        userId = obj['userId']
        return userId == request.user.uuid
