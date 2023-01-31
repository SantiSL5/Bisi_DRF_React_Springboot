# Generated by Django 4.1.5 on 2023-01-31 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0002_remove_bike_slot'),
        ('slots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='bike',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bikes', to='bikes.bike'),
        ),
    ]
