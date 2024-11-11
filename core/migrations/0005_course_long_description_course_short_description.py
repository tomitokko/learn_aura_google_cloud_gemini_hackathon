# Generated by Django 5.0.7 on 2024-08-04 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_course_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='long_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]