# Generated by Django 4.1.7 on 2023-06-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_equipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='comment',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Комментарий'),
        ),
    ]
