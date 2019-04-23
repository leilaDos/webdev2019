import json
from django.shortcuts import render
from api.models import Task,TaskList
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.serializers import TaskListSerializer,TasksSerializer


@csrf_exempt
def task_lists(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method =='POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})

@csrf_exempt
def task_lists_info(request,pk):
    try:
        task_lists_info = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'Error':str(e)},safe=False)
    
    if request.method == 'GET':
        serializer = TaskListSerializer(task_lists_info)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=task_lists_info,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task_lists_info.delete()
        return JsonResponse({})
    return JsonResponse({'error':'bad request'})



@csrf_exempt
def tasks(request,pk):
    try:
        task_lists_info = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'Error':str(e)},safe=False)

    if request.method == 'GET':
        tasks =  task_lists_info.task_set.all()
        serializer = TasksSerializer(tasks,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TasksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error':'bad request'})


@csrf_exempt
def taskInfo(request,pk,pk2):
    try:
        taskInfo = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'Error':str(e)},safe=False)

    if request.method == 'DELETE':
        task = taskInfo.task_set.get(id=pk2)
        task.delete()
        return JsonResponse({},safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        task = taskInfo.task_set.get(id=pk2)
        serializer = TasksSerializer(instance= task,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error)
    return JsonResponse({'Error':'bad request'})
