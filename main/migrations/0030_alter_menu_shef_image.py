# Generated by Django 3.2.8 on 2021-10-27 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_menu_shef_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_shef',
            name='image',
            field=models.ImageField(default='/media/sushi/empty.png', upload_to='sushi'),
        ),
    ]
