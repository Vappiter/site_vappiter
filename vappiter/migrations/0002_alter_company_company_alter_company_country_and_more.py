# Generated by Django 4.1.7 on 2023-05-23 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vappiter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company',
            field=models.CharField(max_length=100, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vappiter.country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.CharField(max_length=100, verbose_name='Страна'),
        ),
    ]