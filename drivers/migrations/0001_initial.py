# Generated by Django 4.2.5 on 2023-09-08 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DriverModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=200)),
                ('driver_phone', models.CharField(max_length=16)),
                ('driver_license', models.CharField(max_length=20)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'driverModel',
                'verbose_name_plural': 'driverModel',
            },
        ),
    ]
