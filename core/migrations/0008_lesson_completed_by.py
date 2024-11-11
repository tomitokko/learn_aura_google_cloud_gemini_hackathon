# Generated by Django 5.0.7 on 2024-08-11 18:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_lesson_raw_content'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='completed_by',
            field=models.ManyToManyField(blank=True, related_name='completed_lessons', to=settings.AUTH_USER_MODEL),
        ),
    ]