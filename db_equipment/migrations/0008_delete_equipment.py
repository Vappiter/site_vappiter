# Generated by Django 4.1.7 on 2023-06-07 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_equipment', '0007_room_equipment_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Equipment',
        ),
    ]
