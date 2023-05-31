from django.contrib import admin

from vappiter.models import Country, Company, Product, Nameproduct, Building, Block, Level, Room, Equipment   

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    # list_display = ('county')
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company','country')
    pass

@admin.register(Nameproduct)
class NameproductAdmin(admin.ModelAdmin):
    # list_display = ('nameproduct')
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('company','nameproduct','type_product')
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

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass
# admin.site.register()
