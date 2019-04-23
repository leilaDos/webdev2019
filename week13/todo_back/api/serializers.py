from rest_framework import serializers
from api.models import Task, TaskList
from datetime import datetime
from datetime import timedelta

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, data):
        return TaskList.objects.create(**data)
    
    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.save()
        return instance
 

class TasksSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # task_list = TaskListSerializer(read_only=True)
    
    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status', 'task_list')
    
    def create(self, data):
        t = data.pop('task_list') 
        return Task.objects.create(task_list=t,**data)
    
    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.created_at = data.get('created_at', instance.created_at)
        instance.due_on = data.get('due_on', instance.due_on)
        instance.status = data.get('status', instance.status)
        instance.task_list = data.get('task_list', instance.task_list)
        instance.save()
        return instance