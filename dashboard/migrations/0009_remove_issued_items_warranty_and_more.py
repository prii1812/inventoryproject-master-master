# Generated by Django 4.1.7 on 2023-04-04 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_issued_items_location_issued_items_warranty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issued_items',
            name='warranty',
        ),
        migrations.RemoveField(
            model_name='issued_items',
            name='warrentyexpire',
        ),
    ]