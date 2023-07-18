from decimal import Decimal

from django.db.models import Q
from django.forms import TextInput
import django_filters

from db_equipment.models import Level

class LevelFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(label='')
    level = django_filters.CharFilter(label='', lookup_expr='istartswith')

    class Meta:
        model = Level
        fields = ['id','level']
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'

    def filter_decimal(self, queryset, name, value):
        # For price and cost, filter based on
        # the following property:
        # value <= result < floor(value) + 1

        lower_bound = "__".join([name, "gte"])
        upper_bound = "__".join([name, "lt"])

        # upper_value = math.floor(value) + Decimal(1)
        upper_value = round(value) + Decimal(1)

        return queryset.filter(**{lower_bound: value,
                                  upper_bound: upper_value})