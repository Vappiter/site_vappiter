# Generated by Django 4.1.7 on 2023-06-05 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vappiter', '0012_rename_type_product_equipment_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='country',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='block',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='building',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='level',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='product',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='room',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='system',
        ),
        migrations.RemoveField(
            model_name='product',
            name='company',
        ),
        migrations.RemoveField(
            model_name='product',
            name='titleproduct',
        ),
        migrations.DeleteModel(
            name='Block',
        ),
        migrations.DeleteModel(
            name='Building',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.DeleteModel(
            name='Level',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='System',
        ),
        migrations.DeleteModel(
            name='Titleproduct',
        ),
    ]
