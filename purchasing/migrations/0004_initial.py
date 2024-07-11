# Generated by Django 4.1.6 on 2023-04-09 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0014_rename_email_organization_mailer_email'),
        ('purchasing', '0003_remove_manufacturer_organization_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100, null=True, unique=True)),
                ('website', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('notes', models.TextField(null=True)),
                ('organization', models.ManyToManyField(to='organizations.organization')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default=('PART', 'Part'), max_length=25)),
                ('units', models.CharField(default=('EACH', 'Each'), max_length=10)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='purchasing.item')),
                ('manufacturer', models.ManyToManyField(to='purchasing.manufacturer')),
                ('organization', models.ManyToManyField(to='organizations.organization')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po', models.IntegerField()),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('shipping', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('notes', models.TextField(null=True)),
                ('organization', models.ManyToManyField(to='organizations.organization')),
            ],
        ),
        migrations.CreateModel(
            name='VendorOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacts', models.JSONField(default=dict, null=True)),
                ('organization', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization')),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='purchasing.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='purchasing.item')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='purchasing.item')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='purchasing.purchaseitem')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchasing.purchaseorder')),
            ],
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchasing.vendor'),
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='vendor',
            field=models.ManyToManyField(to='purchasing.vendor'),
        ),
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_purchase_date', models.DateTimeField(auto_now=True)),
                ('purchase_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchasing.purchaseitem')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='purchasing.item')),
            ],
        ),
    ]
