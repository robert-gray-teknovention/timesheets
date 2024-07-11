# Generated by Django 4.1.6 on 2023-04-12 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchasing', '0013_remove_vendor_organization_vendor_organizations_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='purchase_item',
        ),
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='purchase_order',
        ),
        migrations.RemoveField(
            model_name='purchaseorderitemhistory',
            name='purchase_order_item',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='term',
            field=models.CharField(default='Monthly', max_length=10),
        ),
        migrations.DeleteModel(
            name='PurchaseItem',
        ),
        migrations.DeleteModel(
            name='PurchaseOrderItem',
        ),
        migrations.DeleteModel(
            name='PurchaseOrderItemHistory',
        ),
    ]