from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from api.models import TaskList, Task
from api.serializers import TaskListSerializer,TasksSerializer


class TaskListList(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TasksList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Task.objects.all()
        # return Task.objects.filter(task_list=self.kwargs['pk'])

    def get_serializer_class(self):
        return TasksSerializer


#Doesn't work ... Need To Fix It
class TaskInfo(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Task.objects.filter(task_list=self.kwargs['pk2'])
        # return Task.objects.filter(id=self.kwargs['pk'], task_list=self.kwargs['pk2'])

    def get_serializer_class(self):
        return TasksSerializer
