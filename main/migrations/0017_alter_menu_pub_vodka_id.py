# Generated by Django 3.2.7 on 2021-10-17 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_menu_pub_brendi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_pub_vodka',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]