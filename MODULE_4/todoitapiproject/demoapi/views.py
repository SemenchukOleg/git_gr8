from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from todoitapiproject.logger import logging

logger = logging.getLogger('demoapi')

demo_param = openapi.Parameter('demo_text', openapi.IN_QUERY, description='Example of use the demo_text', required=True, type=openapi.TYPE_STRING )
post_data = openapi.Schema(type='object')
post_data_response = openapi.Schema(type='object')

# Create your views here.
@swagger_auto_schema(method='get', tags=['demo'], manual_parameters=[demo_param])
@swagger_auto_schema(method='post', tags=['demo'], request_body=post_data, responses={201: post_data_response})
@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'GET':
        demo_text = request.GET.get('demo_text')
        logger.debug('Everything is good! GET test')
        return Response (
            {'message': 'API works correctly! Your text is {}'.format(demo_text)},
            status = status.HTTP_200_OK
        )   
    if request.method == 'POST':
        demo_text = request.data.get('demo_text')
        logger.debug('Everything is good! POST test')
        return Response (
            {'message': 'API works correctly POST! Your text is {}'.format(demo_text)},
            status = status.HTTP_201_CREATED
        )   