# Generated by Django 4.2.3 on 2023-09-13 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_reg_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'verbose_name_plural': 'logs'},
        ),
    ]
