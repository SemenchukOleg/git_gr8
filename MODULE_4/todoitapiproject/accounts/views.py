from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from accounts.serializers import MyTokenObtainPairSerializer, UserSerializer
from rest_framework.decorators import (
    api_view, 
    parser_classes, 
    renderer_classes,
    permission_classes
    )
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


# Create your views here.
class MyObtainTokenPairView(TokenObtainPairView):
    permissions_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
            context={'request': request}
            )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })
    
# /api/v1/tasks
@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def create_user(request):
    if not all([request.data.get('first_name'), request.data.get('last_name'), request.data.get('email')]):
        return Response({'message': 'data is wrong'}, status=status.HTTP_400_BAD_REQUEST)
    if request.data.get('password') == request.data.get('password1'):
        serializer_task = UserSerializer(data=request.data)
        if serializer_task.is_valid():
            user = serializer_task.save()
            # JWT logic
            token = Token.objects.get(user=user)
            user_details ={}
            user_details.update({
                'token': token.key,
                'username': user.username,
            })
            login(request=request, user=user)
            return Response(user_details, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'data is wrong'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'password did not match'}, status=status.HTTP_400_BAD_REQUEST)

