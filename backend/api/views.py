from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from api.serializers import UserSerializer


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)