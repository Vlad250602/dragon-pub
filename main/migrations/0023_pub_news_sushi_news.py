# Generated by Django 3.2.7 on 2021-10-24 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20211018_0324'),
    ]

    operations = [
        migrations.CreateModel(
            name='pub_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название новости')),
                ('spec', models.CharField(blank=True, max_length=300, verbose_name='Новость')),
                ('date', models.CharField(blank=True, max_length=20, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Новости паб',
                'verbose_name_plural': 'новость',
            },
        ),
        migrations.CreateModel(
            name='sushi_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название новости')),
                ('spec', models.CharField(blank=True, max_length=300, verbose_name='Новость')),
                ('date', models.CharField(blank=True, max_length=20, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Новости суши',
                'verbose_name_plural': 'новость',
            },
        ),
    ]
