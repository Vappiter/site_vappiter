"""vappiter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework import routers

from db_equipment import views
from db_equipment.views import CompanyView, CompanyView, Equipment

# router = routers.DefaultRouter()
# router.register(r'company/', CompanyView.as_view())

# app_name = 'vappiter'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='index'),
    path('index', views.index, name='index'),
    path('country', views.vcountry, name='country'),
    # path('company/', CompanyView.as_view()),
    path('api/company/', CompanyView.as_view()),
    path('equipment/', views.vequipment, name='equipment')
       
] 

# urlpatterns += router.urls
