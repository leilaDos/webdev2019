from django.urls import path, re_path
from api import views

urlpatterns = [

#     path('task_lists', views.task_lists),
#     path('task_lists/<int:pk>/',views.task_lists_info),
#     path('task_lists/<int:pk>/tasks',views.tasks),
#     path('task_lists/<int:pk>/tasks/<int:pk2>',views.taskInfo)
    path('task_lists', views.TaskListList.as_view()),
    path('task_lists/<int:pk>/', views.TaskListInfo.as_view()),
    path('task_lists/<int:pk>/tasks', views.TasksList.as_view()),
    path('task_lists/<int:pk>/tasks/<int:pk2>', views.TaskInfo.as_view())
]
