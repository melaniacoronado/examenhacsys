# Generated by Django 3.1.7 on 2021-04-22 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_auto_20210421_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidencia',
            name='fecha',
            field=models.DateField(),
        ),
    ]
