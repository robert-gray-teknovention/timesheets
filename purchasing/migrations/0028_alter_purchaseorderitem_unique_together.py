# Generated by Django 4.1.6 on 2023-04-20 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchasing', '0027_remove_purchaseorder_po_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='purchaseorderitem',
            unique_together={('purchase_order', 'purchase_item')},
        ),
    ]
