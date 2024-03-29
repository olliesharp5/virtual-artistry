# Generated by Django 4.2.10 on 2024-02-29 14:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0006_art_art_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='art_image',
            field=cloudinary.models.CloudinaryField(default='art_placeholder', max_length=255, verbose_name='art_image'),
        ),
    ]
