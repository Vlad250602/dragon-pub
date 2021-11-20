# Generated by Django 3.2.7 on 2021-10-06 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20211007_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_gunkan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('weight', models.CharField(max_length=10, verbose_name='Вес')),
                ('spec', models.CharField(blank=True, max_length=200, verbose_name='Состав')),
                ('price', models.CharField(max_length=10, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Гункан',
                'verbose_name_plural': 'Гункан',
            },
        ),
        migrations.CreateModel(
            name='Menu_sashimi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('weight', models.CharField(max_length=10, verbose_name='Вес')),
                ('spec', models.CharField(blank=True, max_length=200, verbose_name='Состав')),
                ('price', models.CharField(max_length=10, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Сашими',
                'verbose_name_plural': 'Сашими',
            },
        ),
        migrations.AlterModelOptions(
            name='menu_nigiri',
            options={'verbose_name': 'Нигири', 'verbose_name_plural': 'Нигири'},
        ),
        migrations.AlterModelOptions(
            name='menu_sets',
            options={'verbose_name': 'Сет', 'verbose_name_plural': 'Сеты'},
        ),
    ]