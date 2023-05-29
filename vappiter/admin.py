from django.contrib import admin

from vappiter.models import Country, Company, Product   

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    # list_display = ('county')
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company','country')
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('company','title_product','type_product')
    pass
# admin.site.register()
