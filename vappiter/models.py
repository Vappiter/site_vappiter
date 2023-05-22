from django.db import models

class Country(models.Model):
    """Страны производители оборудования"""
    name_country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name_country