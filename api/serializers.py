from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import TodoList

User = get_user_model()

class TodoListSerializer(serializers.ModelSerializer):

	class Meta:
		model = TodoList
		fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'email',
		]

		extra_kwargs = {
			"password": {
				"write_only": True
			}
		}

	def create(self, validated_data):
		username = validated_data['username']
		email = validated_data['email']
		password = validated_data['password']
		user = User(
				username = username,
				email = email,

			)
		user.set_password(password)
		user.save()

		return validated_data