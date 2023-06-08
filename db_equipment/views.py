from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from db_equipment.serializers import CompanySerializer

from db_equipment.models import Country, Company, Equipment, Level


def index(request):
  return render(request, 'index.html') 

def vcountry(request):
    country = Country.objects.all()
    return render(request, 'country.html',{'country':country})

class CompanyView(APIView):
   
    def get(self, request, format=None):
      queryset = Company.objects.all()
      serializer_class = CompanySerializer(queryset, many=True)
      return Response (serializer_class.data)
#    def get(self, request):
#       company = Company.objects.all()
#       return Response ({'company': company})

def equipment(request):
   equipment = Equipment.objects.all()
   return render(request, 'equipment.html',{'equipment': equipment})
