# Generated by Django 4.1.7 on 2023-06-07 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_equipment', '0002_equipment_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box', models.CharField(max_length=20, verbose_name='Шкаф')),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='room',
            field=models.CharField(max_length=10, verbose_name='Помещение'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='box',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_equipment.box', verbose_name='Шкаф'),
        ),
    ]
