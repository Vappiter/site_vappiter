from django.db import models

class Country(models.Model):
    """Страны производители оборудования"""
    country = models.CharField(max_length=100, verbose_name='Страна')

    def __str__(self) -> str:
        return self.name_country
    
class Company(models.Model):
    """Производители оборудования"""
    company = models.CharField(max_length=100, verbose_name='Компания')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')
