from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('register',views.user_register),
    path('user_login',views.user_login),
    path('user_logout',views.user_logout),
]