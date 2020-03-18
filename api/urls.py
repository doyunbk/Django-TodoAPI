from django.urls import path
from . import views


from django.http import HttpResponse

from . views import RegisterationAPI

urlpatterns = [
    path('', views.index, name="api_index"), 
    path('register/', RegisterationAPI.as_view(), name="register"),   
    path('todolist/', views.todoList, name="todo_list"),
    path('viewtask/<int:pkey>', views.viewTask, name="view_task"),
    path('createtask/', views.createTask, name="create_task"),
    path('updatetask/<int:pkey>', views.updateTask, name="update_task"),
    path('deletetask/<int:pkey>', views.deleteTask, name="delete_task"),

]
