# Generated by Django 4.1.7 on 2023-03-30 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_country_latitude_alter_country_longitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='emblem',
            field=models.ImageField(blank=True, null=True, upload_to='emblems'),
        ),
        migrations.AlterField(
            model_name='country',
            name='flag',
            field=models.ImageField(blank=True, null=True, upload_to='flags'),
        ),
    ]
