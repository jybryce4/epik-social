# Generated by Django 3.0.6 on 2020-05-30 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200530_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.TextField(default='John', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.TextField(default='Doe', max_length=200),
        ),
    ]
