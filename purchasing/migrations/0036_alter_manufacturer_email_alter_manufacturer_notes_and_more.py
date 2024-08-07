# Generated by Django 4.1.6 on 2023-05-22 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchasing', '0035_vendor_notes_remove_manufacturer_organization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
