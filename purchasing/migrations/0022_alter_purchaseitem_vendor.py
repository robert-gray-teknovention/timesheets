# Generated by Django 4.1.6 on 2023-04-12 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchasing', '0021_remove_subscription_term_alter_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseitem',
            name='vendor',
            field=models.ManyToManyField(to='purchasing.vendor'),
        ),
    ]
