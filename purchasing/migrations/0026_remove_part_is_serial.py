# Generated by Django 4.1.6 on 2023-04-13 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchasing', '0025_rename_last_purchase_date_purchaseorderitemhistory_status_change_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='is_serial',
        ),
    ]
