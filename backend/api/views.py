from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.response import Response
import api.serializers as serializers
import api.models as models
from django.db.utils import IntegrityError


class UsersView(APIView):
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
            else:
                response = {
                    'uuid': user.uuid,
                    'success': True
                }
            return Response(response, status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
