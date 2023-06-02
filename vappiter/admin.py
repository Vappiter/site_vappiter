from django.contrib import admin

from .models import Country, Company, Titleproduct, Product, Building, Block, Level, Room, System  

# Nameproduct, Building, Block, Level, Room, System   

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company','country')
    pass

@admin.register(Titleproduct)
class TitleproductAdmin(admin.ModelAdmin):
    pass 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('company','titleproduct','product')
    pass

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    pass

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    pass

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

# # @admin.register(Equipment)
# # class EquipmentAdmin(admin.ModelAdmin):
# #     pass

@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    pass
# admin.site.register()
