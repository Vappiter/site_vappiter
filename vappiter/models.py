from django.db import models

class Country(models.Model):
    """Страны производители оборудования"""
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name_country
    
class Company(models.Model):
    """Производители оборудования"""
    company = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
