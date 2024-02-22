# Generated by Django 4.2.10 on 2024-02-22 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('about', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year', models.DateField()),
                ('condition', models.IntegerField(choices=[(0, 'Excellent'), (1, 'Good'), (2, 'Worn')], default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
