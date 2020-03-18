from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers import TodoListSerializer, RegisterSerializer

from .models import TodoList
# Create your views here.


@api_view(['GET'])
def index(request):

	urls = {
		'register': '/register',
		'todoList': '/todolist',
		'viewTask': '/viewtask/<int:pkey>',
		'createTask': '/createtask',
		'updateTask': '/updatetask/<int:pkey>',
		'deleteTask': '/deletetask/<int:pkey>',
	}

	return Response(urls)

@api_view(['GET'])
def todoList(request):
	todoLists = TodoList.objects.all()
	serializer = TodoListSerializer(todoLists, many=True)

	return Response(serializer.data)


@api_view(['GET'])
def viewTask(request, pkey):
	task = TodoList.objects.get(id=pkey)
	serializer = TodoListSerializer(task, many=False)

	return Response(serializer.data)


@api_view(['POST'])
def createTask(request):
	serializer = TodoListSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
		serializer.save(user=request.user)


	return Response(serializer.data)


@api_view(['POST'])
def updateTask(request, pkey):
	task = TodoList.objects.get(id=pkey)
	serializer = TodoListSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteTask(request, pkey):
	task = TodoList.objects.get(id=pkey)
	user = request.user
	if task.user != user:
		return Response({'response': 'You must be an owener'})
	else:
		task.delete()
	context = "task is deleted"

	return Response(context)


User = get_user_model()

class RegisterationAPI(CreateAPIView):
	serializer_class = RegisterSerializer
	queryset = User.objects.all()


class CreatedBy(ListCreateAPIView):

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)





