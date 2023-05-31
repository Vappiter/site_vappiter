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
    
class Building(models.Model):
    """Здание"""
    building = models.CharField(max_length=25, verbose_name='Здание')    

    def __str__(self) -> str:
        return self.building

class Block(models.Model):
    """Блок"""
    block = models.CharField(max_length=4, verbose_name='Блок')
    # building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='Здание')

    def __str__(self) -> str:
        return self.block

class Level(models.Model):
    """Этаж"""
    level = models.CharField(max_length=5, verbose_name='Этаж')

    def __str__(self) -> str:
        return self.level

class Room(models.Model):
    """Помещение"""
    room = models.CharField(max_length=10, verbose_name='Этаж')    

class Equipment(models.Model):
    """Оборудование"""
    type_product = models.ForeignKey(Product, verbose_name=("Модель изделия"), on_delete=models.CASCADE, null=True)
    building = models.ForeignKey(Building, verbose_name=("Здание"), on_delete=models.CASCADE, null=True)
    block = models.ForeignKey(Block, verbose_name=("Блок"), on_delete=models.CASCADE, null=True)
    level = models.ForeignKey(Level, verbose_name=("Уровень"), on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, verbose_name=("Помещение"), on_delete=models.CASCADE, null=True)
    sernum = models.CharField(max_length=20, verbose_name='Серийный номер')


    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
  
        

    