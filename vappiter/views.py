from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Country, Company


def index(request):
  return render(request, 'index.html') 

def vcountry(request):
    country = Country.objects.all()
    return render(request, 'country.html',{'country':country})

class CompanyView(APIView):
   def get(self, request):
      company = Company.objects.all()
      return Response ({'company': company})
