from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import User



class UserListApiView(APIView):
    def get(self, request):

        data = {
            'massage': 'ok',
            'status': 'backendan salomlar'
        }
        return Response(data, status=status.HTTP_200_OK)
