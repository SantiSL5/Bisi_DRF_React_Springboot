# Generated by Django 4.1.5 on 2023-01-31 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='slot',
        ),
    ]
