# Generated by Django 4.2.10 on 2024-02-29 13:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_artistprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistprofile',
            name='artist_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='artist_image'),
        ),
    ]