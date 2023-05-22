from django.contrib import admin

from vappiter.models import Country, Company

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    # list_display = ('county')
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    # list_display = ('country', 'company')
    pass

# admin.site.register()
