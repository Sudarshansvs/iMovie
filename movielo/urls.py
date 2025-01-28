"""
URL configuration for iMovie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from movielo import views
app = "movielo"
urlpatterns = [
    path('add',views.dest_add,name='add_destination'),
    path('dest/<int:dest_id>',views.dest_details),
    path('dest/<int:id>',views.dest_details,name='details'),
    path('hp2',views.homepage2),
    path('homepage', views.homepage),
    path('login', views.login),
    path('views', views.view_profile),
    path('edit', views.edit_profile),
    path('delete', views.delete_profile),
    path('api/dests/',views.get_all_destinations)
]
