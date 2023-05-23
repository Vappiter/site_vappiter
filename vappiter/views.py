from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from .models import Country

def vcountry(request):
    country = Country.objects.all()
    return render(request, 'country.html',{'country':country})
