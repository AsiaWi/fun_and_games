# Generated by Django 3.2.21 on 2023-10-03 17:27

from django.conf import settings
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('playground', '0003_auto_20230922_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='featured_image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[600, None], upload_to='activities/'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
