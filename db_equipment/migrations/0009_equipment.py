# Generated by Django 4.1.7 on 2023-06-07 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_equipment', '0008_delete_equipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sernum', models.CharField(blank=True, max_length=30, null=True, verbose_name='Серийный номер')),
                ('comment', models.TextField(blank=True, max_length=300, null=True, verbose_name='Комментарий')),
                ('block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_equipment.block', verbose_name='Блок')),
                ('box', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_equipment.box', verbose_name='Шкаф')),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_equipment.building', verbose_name='Здание')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_equipment.level', verbose_name='Уровень')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_equipment.product', verbose_name='Модель изделия')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_equipment.room', verbose_name='Помещение')),
                ('system', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_equipment.system', verbose_name='Система КИТСО')),
            ],
        ),
    ]
