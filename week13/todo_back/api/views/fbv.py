from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import TaskList,Task
from api.serializers import TaskListSerializer,TasksSerializer

@api_view(['GET','POST'])
def task_lists(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'error': 'bad request'})


@api_view(['GET', 'PUT', 'DELETE'])
def task_lists_info(request, pk):
    try:
        task_lists_info = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({'Error': str(e)})

    if request.method == 'GET':
        serializer = TaskListSerializer(task_lists_info)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer(instance=task_lists_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        task_lists_info.delete()
        return Response({},status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'bad request'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
def tasks(request,pk):
    try:
        task_lists_info = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({'Error':str(e)})

    if request.method == 'GET':
        tasks =  task_lists_info.task_set.all()
        serializer = TasksSerializer(tasks,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    return Response({'error':'bad request'})


@api_view(['DELETE', 'PUT'])
def taskInfo(request,pk,pk2):
    try:
        taskInfo = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({'Error':str(e)})

    if request.method == 'DELETE':
        task = taskInfo.task_set.get(id=pk2)
        task.delete()
        return Response({})
    elif request.method == 'PUT':
        task = taskInfo.task_set.get(id=pk2)
        serializer = TasksSerializer(instance= task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    return Response({'Error':'bad request'})
