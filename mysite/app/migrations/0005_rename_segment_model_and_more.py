# Generated by Django 4.0.4 on 2022-04-22 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_brand_segment_vehicle_remove_vehicle_segment_brand_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Segment',
            new_name='Model',
        ),
        migrations.RenameField(
            model_name='model',
            old_name='segment_name',
            new_name='model_name',
        ),
    ]