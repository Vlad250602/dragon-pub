# Generated by Django 3.2.7 on 2021-10-17 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_menu_pub_vodka_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_pub_vodka',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
