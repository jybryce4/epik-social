# Generated by Django 3.0.6 on 2020-05-30 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.TextField(default='John'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.TextField(default='Doe'),
        ),
        migrations.AddField(
            model_name='profile',
            name='tagline',
            field=models.TextField(default="I'm EPIC"),
        ),
    ]
