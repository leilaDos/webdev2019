from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from api.models import TaskList,Task
from api.serializers import TaskListSerializer,TasksSerializer


class TaskListList(APIView):
    def get(self, request):
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class TaskListInfo(APIView):
    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist :
            raise Http404

    def get(self, request, pk):
        task_lists_info = self.get_object(pk)
        serializer = TaskListSerializer(task_lists_info)
        return Response(serializer.data)

    def put(self, request, pk):
        task_lists_info = self.get_object(pk)
        serializer = TaskListSerializer(instance=task_lists_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        task_lists_info = self.get_object(pk)
        task_lists_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Tasks(APIView):
    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist :
            raise Http404

    def get(self, request,pk):
        task_lists_info = self.get_object(pk)
        tasks = task_lists_info.task_set.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Task(APIView):
    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def delete(self, request, pk, pk2):
        task_info = self.get_object(pk)
        task = task_info.task_set.get(id=pk2)
        task.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, pk2):
        task_info = self.get_object(pk)
        task = task_info.task_set.get(id=pk2)
        serializer = TasksSerializer(instance= task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
