from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.viewsets import ViewSet
from .serializers import RegisterUserSerializers


def custom_response(status, technical_message='', message='', data='', *args, **kwargs):
    return Response({
        "status": status,
        "technical_message": technical_message,
        "message": message,
        "data": data
    })
    

class RegisterViewset(ViewSet):
    def post(self, request):
        serializer = RegisterUserSerializers(request.data)

        if serializer.is_valid():
            pass

        custom_response(
            status=HTTP_400_BAD_REQUEST,
            technical_message=serializer.errors,
            message="Something went wrong, please confirm credientials."
            )


class LoginViewset(ViewSet):
    def post(self, request):

        print(request.headers, "-------------------", request.META)
        
        return custom_response(status=HTTP_200_OK)