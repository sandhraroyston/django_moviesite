# Generated by Django 4.2 on 2023-04-25 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movielist',
            name='img',
        ),
    ]