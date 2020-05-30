# Generated by Django 3.0.6 on 2020-05-30 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='John', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Doe', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tagline',
            field=models.CharField(default="I'm EPIC", max_length=200),
        ),
    ]
