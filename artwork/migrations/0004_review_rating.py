# Generated by Django 4.2.10 on 2024-02-26 14:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0003_alter_art_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]
