# Generated by Django 5.1.4 on 2025-01-03 10:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0003_comment_created_at_comment_updated_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replay',
            field=models.ManyToManyField(related_name='comment_replay', to=settings.AUTH_USER_MODEL),
        ),
    ]
