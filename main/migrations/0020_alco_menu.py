# Generated by Django 3.2.7 on 2021-10-17 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_menu_pub_vodka_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='alco_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Alco_menu',
                'verbose_name_plural': 'Alco_menu',
            },
        ),
    ]
