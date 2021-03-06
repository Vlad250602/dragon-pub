# Generated by Django 3.2.8 on 2021-10-27 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_menu_kalif_kunj_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_dragon',
            name='image',
            field=models.ImageField(default='sushi/empty.png', upload_to='sushi'),
        ),
        migrations.AddField(
            model_name='menu_gunkan',
            name='image',
            field=models.ImageField(default='sushi/empty.png', upload_to='sushi'),
        ),
        migrations.AddField(
            model_name='menu_kalif_tobiko',
            name='image',
            field=models.ImageField(default='sushi/empty.png', upload_to='sushi'),
        ),
        migrations.AddField(
            model_name='menu_nigiri',
            name='image',
            field=models.ImageField(default='sushi/empty.png', upload_to='sushi'),
        ),
        migrations.AddField(
            model_name='menu_sashimi',
            name='image',
            field=models.ImageField(default='sushi/empty.png', upload_to='sushi'),
        ),
        migrations.AddField(
            model_name='menu_sets',
            name='image',
            field=models.ImageField(default='sushi/empty.png', upload_to='sushi'),
        ),
    ]
