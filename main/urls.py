from django.urls import path
from . import views


from django.http import HttpResponse


urlpatterns = [
    path('', views.user_login, name="login"),  
    path('index', views.index, name="index"),
]
