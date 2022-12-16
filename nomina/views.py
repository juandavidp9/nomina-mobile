from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from knox.auth import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import UserSerializer, RegisterSerializer


# Create your views here.
@api_view(['POST'])
def login(self, request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    return Response ({
        "user": UserSerializer(user, context = self.get_serializer_context()).data,
        "message": "Login exitoso",
        'token': AuthToken.objects.create(user)
    })

        

@api_view(['POST'])
def registro(self, request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response (
        {"user": UserSerializer(user, context= self.get_serializer_context()).data,
        "message": "Registro exitoso",
        "token": AuthToken.objects.create(user)}
    )
