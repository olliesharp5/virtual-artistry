# Generated by Django 4.2.10 on 2024-02-29 14:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_artistprofile_artist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistprofile',
            name='artist_image',
            field=cloudinary.models.CloudinaryField(default='artist_placeholder', max_length=255, verbose_name='artist_image'),
        ),
    ]
