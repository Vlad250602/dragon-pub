# Generated by Django 3.2.7 on 2021-10-17 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_menu_pub_vodka_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_pub_vodka',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
