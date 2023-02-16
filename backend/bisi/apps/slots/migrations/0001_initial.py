# Generated by Django 4.1.5 on 2023-02-16 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bikes', '0001_initial'),
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField(db_index=True)),
                ('warning', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('bike', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bikes', to='bikes.bike')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='stations.station')),
            ],
            options={
                'verbose_name_plural': 'Slots',
                'unique_together': {('number', 'station')},
            },
        ),
    ]
