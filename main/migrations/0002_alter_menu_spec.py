# Generated by Django 3.2.7 on 2021-10-05 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='spec',
            field=models.CharField(max_length=100, verbose_name='Состав'),
        ),
    ]
