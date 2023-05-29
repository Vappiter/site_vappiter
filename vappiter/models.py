from django.db import models

class Country(models.Model):
    """Страны производители оборудования"""
    country = models.CharField(max_length=100, verbose_name='Страна')

    def __str__(self) -> str:
        return self.country
    
class Company(models.Model):
    """Производители оборудования"""
    company = models.CharField(max_length=100, verbose_name='Компания')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')

    def __str__(self) -> str:
        return self.company

class Nameproduct(models.Model):
    """Наименование изделия"""
    nameproduct = models.CharField(max_length=100, verbose_name='Наименование изделия')
    
    
class Product(models.Model):
    """Модель оборудования"""
    company = models.ForeignKey(Company, verbose_name=("Производитель"), on_delete=models.CASCADE, null=True)
    nameproduct = models.ForeignKey(Nameproduct, verbose_name=("Наименование изделия"), on_delete=models.CASCADE, null=True)
    type_product = models.CharField(max_length=50, verbose_name='Модель изделия')
    
    

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
  
        

    