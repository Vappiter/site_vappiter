import django_tables2 as tables
from db_equipment.models import Equipment

class Test(tables.Table):
    class Meta:
        model = Equipment
        # db_table = ''
        # managed = True
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        show_header = False
        template_name = 'tables/test.html'