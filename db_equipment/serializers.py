from rest_framework import serializers

from db_equipment.models import Company

class CompanySerializer(serializers.Serializer):

    class Meta:
        model = Company
        fields = ['company_id','company']

    # company = serializers.CharField(max_length=100, verbose_name='Компания')
    # country = serializers.CharField(source='country.country', verbose_name='Страна')