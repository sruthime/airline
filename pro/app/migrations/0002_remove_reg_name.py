# Generated by Django 4.2.3 on 2023-09-13 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='name',
        ),
    ]
