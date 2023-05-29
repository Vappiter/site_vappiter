from django.contrib import admin

from vappiter.models import Country, Company, Product, Nameproduct   

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
# admin.site.register()
