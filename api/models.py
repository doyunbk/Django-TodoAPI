from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.conf import settings

class TodoList(models.Model):

	subject = models.CharField(max_length=20)
	status = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.subject