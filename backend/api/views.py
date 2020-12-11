from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.response import Response
import api.serializers as serializers
import api.models as models
from django.db.utils import IntegrityError
from rest_framework.permissions import AllowAny
# TODO input validation


class UsersView(APIView):
    permission_classes = [AllowAny]

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


class SpecificUsersView(APIView):
    def post(self, request, uuid, format=None):
        user = request.user

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
