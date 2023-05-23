from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from .models import Country


def index(request):
  return render(request, 'index.html') 

def vcountry(request):
    country = Country.objects.all()
    return render(request, 'country.html',{'country':country})

