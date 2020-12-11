from django.db.utils import IntegrityError
from rest_framework import authentication, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import api.models as models
import api.serializers as serializers
import api.permissions as permissions
# TODO input validation


class ContactsView(APIView):
    """
    /organizations/{orgId}/contacts/
    """
    permission_classes = [permissions.IsOrganizationMember]
    allowed_methods = ['GET', 'POST']

    def get(self, request, orgId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, orgId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ContactView(APIView):
    """
    /organizations/{orgId}/contacts/{contactId}/
    """
    permission_classes = [permissions.IsOrganizationMember]
    allowed_methods = ['GET', 'POST', 'DELETE']

    def get(self, request, orgId, contactId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, orgId, contactId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, orgId, contactId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ContactNotesView(APIView):
    """
    /organizations/{orgId}/contacts/{contactId}/notes/
    """
    permission_classes = [permissions.IsOrganizationMember]
    allowed_methods = ['POST']

    def post(self, request, orgId, contactId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ContactNoteView(APIView):
    """
    /organizations/{orgId}/contacts/{contactId}/notes/{noteId}/
    """
    permission_classes = [permissions.IsOrganizationMember]
    allowed_methods = ['DELETE']

    def delete(self, request, orgId, contactId, noteId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class MembersView(APIView):
    """
    /organizations/{orgId}/members/
    """
    permission_classes = [permissions.IsOrganizationMember]
    allowed_methods = ['GET']

    def get(self, request, orgId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class MemberView(APIView):
    """
    /organizations/{orgId}/members/{memberId}/
    """
    permission_classes = [permissions.IsOrganizationAdminOrReadOnly]
    allowed_methods = ['GET', 'DELETE']

    def get(self, request, orgId, memberId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, orgId, memberId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class RequestsView(APIView):
    """
    /organizations/{orgId}/requests/
    """
    permission_classes = [permissions.IsOrganizationAdminOrPostOnly]
    allowed_methods = ['GET', 'POST']

    def get(self, request, orgId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, orgId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class RequestView(APIView):
    """
    /organizations/{orgId}/requests/{requestId}/
    """
    permission_classes = [permissions.IsOrganizationAdmin]
    allowed_methods = ['GET', 'POST', 'DELETE']

    def get(self, request, orgId, requestId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, orgId, requestId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, orgId, requestId):
        # TODO
        obj = {'orgId': orgId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UsersView(APIView):
    """
    /users/
    """
    permission_classes = [AllowAny]
    allowed_methods = ['POST']

    def post(self, request, format=None):
        data = serializers.UserAdditionSerializer(data=request.data)
        if data.is_valid():
            email = data.data['email']
            password = data.data['password']
            first_name = data.data['first_name']
            last_name = data.data['last_name']

            try:
                user = models.User.objects.create_user(email,
                                                       password,
                                                       first_name=first_name,
                                                       last_name=last_name)
            except IntegrityError:
                response = {
                    'success': False,
                    'errorMessage': 'Database integrity exception'
                }
                code = status.HTTP_400_BAD_REQUEST
            else:
                response = {
                    'uuid': user.uuid,
                    'success': True
                }
                code = status.HTTP_201_CREATED
            return Response(response, code)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    """
    /users/{userId}/
    """
    permission_classes = [permissions.OwnsAccount]
    allowed_methods = ['GET', 'POST', 'DELETE']

    def get(self, request, userId):
        # TODO
        obj = {'userId': userId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, userId):
        obj = {'userId': userId}
        self.check_object_permissions(request, obj)

        user = request.user
        if userId != user.uuid:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        data = serializers.UserUpdateSerializer(data=request.data)
        if data.is_valid():
            if 'first_name' in data.data:
                user.first_name = data.data['first_name']
            if 'last_name' in data.data:
                user.last_name = data.data['last_name']
            if 'password' in data.data:
                user.set_password(data.data['password'])

            user.save()

            response = {
                'success': True
            }

            return Response(response, status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, userId):
        # TODO
        obj = {'userId': userId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class NotificationsView(APIView):
    """
    /users/{userId}/notifications/
    """
    permission_classes = [permissions.OwnsAccount]
    allowed_methods = ['GET']

    def get(self, request, userId):
        # TODO
        obj = {'userId': userId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class NotificationView(APIView):
    """
    /users/{userId}/notifications/{notificationId}/
    """
    permission_classes = [permissions.OwnsAccount]
    allowed_methods = ['GET', 'DELETE']

    def get(self, request, userId, notificationId):
        # TODO
        obj = {'userId': userId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, userId, notificationId):
        # TODO
        obj = {'userId': userId}
        self.check_object_permissions(request, obj)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
