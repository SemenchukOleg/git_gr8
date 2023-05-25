from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def test(request):
    return Response (
        {'message': 'API works correctly!',},
        status = status.HTTP_200_OK
    )   