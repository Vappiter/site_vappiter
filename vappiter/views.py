from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from .models import Country

def index(request):
    country = Country.objects.all()
