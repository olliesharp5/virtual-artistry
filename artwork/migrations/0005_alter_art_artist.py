# Generated by Django 4.2.10 on 2024-02-26 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_artistprofile_slug'),
        ('artwork', '0004_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art_posts', to='artists.artistprofile'),
        ),
    ]
