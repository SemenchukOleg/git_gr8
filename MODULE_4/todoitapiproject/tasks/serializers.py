from rest_framework import serializers
from tasks.models import Task
from accounts.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Task
        #fields = '__all__'
        fields = ['id', 'title', 'description', 'priority', 'is_completed', 'short_description', 'user']
        

class TaskNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'short_description', 'user']