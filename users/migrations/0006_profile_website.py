# Generated by Django 3.0.6 on 2020-05-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200530_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(default='example.com'),
        ),
    ]
