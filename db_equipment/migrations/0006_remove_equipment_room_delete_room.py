# Generated by Django 4.1.7 on 2023-06-07 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_equipment', '0005_alter_block_block_alter_room_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='room',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
