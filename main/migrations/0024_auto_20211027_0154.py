# Generated by Django 3.2.7 on 2021-10-26 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_pub_news_sushi_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pub_news',
            options={'verbose_name': 'новость', 'verbose_name_plural': 'Новости паб'},
        ),
        migrations.AlterModelOptions(
            name='sushi_news',
            options={'verbose_name': 'новость', 'verbose_name_plural': 'Новости суши'},
        ),
        migrations.AlterField(
            model_name='sushi_news',
            name='spec',
            field=models.TextField(blank=True, max_length=300, verbose_name='Новость'),
        ),
    ]
