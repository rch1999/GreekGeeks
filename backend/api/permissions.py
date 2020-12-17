from rest_framework import permissions


class IsOrganizationAdmin(permissions.BasePermission):
    """
    A view with this permission can only be accessed by an admin of the 
    organization that the view is for.
    """
    def has_object_permission(self, request, view, obj):
        if not(request.user and request.user.is_authenticated):
            return False

        orgId = obj['orgId']
        user = request.user
        is_admin = user.admin_of.filter(uuid=orgId).count() > 0
        return is_admin


class IsOrganizationMember(permissions.BasePermission):
    """
    A view with this permission can only be accessed by members of the
    organization that the view is for.
    """
    def has_object_permission(self, request, view, obj):
        if not(request.user and request.user.is_authenticated):
            return False

        orgId = obj['orgId']
        user = request.user
        is_member = user.member_of.filter(uuid=orgId).count() > 0
        return is_member


class IsOrganizationAdminOrReadOnly(permissions.BasePermission):
    """
    A view with this permission can be read from by members of the organization
    or written to (e.g. POST) by an organization admin.
    """
    SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

    def has_object_permission(self, request, view, obj):
        if not(request.user and request.user.is_authenticated):
            return False

        orgId = obj['orgId']
        user = request.user
        is_member = user.member_of.filter(uuid=orgId).count() > 0
        is_admin = user.admin_of.filter(uuid=orgId).count() > 0

        if is_admin:
            return True
        elif is_member:
            return request.method in IsOrganizationAdminOrReadOnly.SAFE_METHODS
        else:
            return False


class IsOrganizationAdminOrPostOnly(permissions.BasePermission):
    """
    A view with this permission can be read by organization admins but posted
    by anyone that is authenticated.
    """
    def has_object_permission(self, request, view, obj):
        if not(request.user and request.user.is_authenticated):
            return False

        orgId = obj['orgId']
        user = request.user
        is_admin = user.admin_of.filter(uuid=orgId).count() > 0

        userId = obj['userId']
        return is_admin or (request.method == 'POST' and userId == user.uuid)


class IsOrganizationAdminOrDeleteOnly(permissions.BasePermission):
    """
    A view with this permission can be deleted by the owner of the resource,
    while an organization admin whose organization owns the resource can do
    anything with it.
    """
    def has_object_permission(self, request, view, obj):
        if not(request.user and request.user.is_authenticated):
            return False

        orgId = obj['orgId']
        user = request.user
        is_admin = user.admin_of.filter(uuid=orgId).count() > 0

        userId = obj['userId']
        return is_admin or (request.method == 'DELETE' and userId == user.uuid)


class OwnsAccount(permissions.BasePermission):
    """
    A view with this permission can be accessed by the owner of the account
    to which the resource refers.
    """
    def has_object_permission(self, request, view, obj):
        if not(request.user and request.user.is_authenticated):
            return False

        userId = obj['userId']
        return userId == request.user.uuid
