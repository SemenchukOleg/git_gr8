from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes, renderer_classes
from rest_framework.response import Response
from tasks.serializers import TaskSerializer, TaskNewSerializer
from tasks.models import Task
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

# Create your views here.
# /api/v1/tasks
@api_view(['GET', 'POST'])
@parser_classes([JSONParser, FormParser])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def get_task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer_tasks = TaskSerializer(tasks, many=True)
        return Response(serializer_tasks.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        #Получить данные
        data = request.data
        selializer_new_task = TaskNewSerializer(data=data)
        if selializer_new_task.is_valid():
            selializer_new_task.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'data is wrong'}, status=status.HTTP_400_BAD_REQUEST)

# /api/v1/tasks/task/<int:id>
@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([JSONParser, FormParser])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def get_or_update_task_by_id(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer_task = TaskSerializer(task)
        return Response(serializer_task.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        #Получить данные
        data = request.data
        #выполнить обновление существующей задачи
        serializer_task = TaskSerializer(task, data=data)
        if serializer_task.is_valid():
            serializer_task.save()
            return Response(serializer_task.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'data is wrong'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#api/v1/tasks/priorities
@api_view(['GET'])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def get_task_priorities_list(request):
    if request.method == 'GET':
        task_priorities = Task.get_priorities_list()
        return Response(task_priorities, status=status.HTTP_200_OK)
    
# /api/v1/tasks/complete-all/
@api_view(['PUT'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def complete_all_tasks(request):
    if request.method == 'PUT':
        tasks = Task.objects.filter(is_completed=False)
        for task in tasks:
            task.is_completed = True
            task.save()
        return Response(status=status.HTTP_200_OK)
    
# /api/v1/tasks/uncomplete-all/
@api_view(['PUT'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def uncomplete_all_tasks(request):
    if request.method == 'PUT':
        tasks = Task.objects.filter(is_completed=True)
        for task in tasks:
            task.is_completed = False
            task.save()
        return Response(status=status.HTTP_200_OK)
    
# /api/v1/tasks/delete-all/
@api_view(['DELETE'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def delete_all_tasks(request):
    if request.method == 'DELETE':
        tasks = Task.objects.all()
        for task in tasks:
            task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    