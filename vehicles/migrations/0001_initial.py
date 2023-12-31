# Generated by Django 4.2.5 on 2023-09-08 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_plate', models.CharField(max_length=10)),
                ('vehicle_brand', models.CharField(max_length=100)),
                ('vehicle_model', models.CharField(default='ae', max_length=100)),
                ('vehicle_oil_change_km', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'vehicleModel',
                'verbose_name_plural': 'vehicleModel',
            },
        ),
    ]
