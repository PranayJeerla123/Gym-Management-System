# Generated by Django 5.0.1 on 2024-02-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='membershipplan',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
