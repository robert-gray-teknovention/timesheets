# Generated by Django 4.1.6 on 2023-04-05 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('timesheets', '0015_timesheetentry_hourly_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('date_submitted', models.DateTimeField(null=True)),
                ('date_approved', models.DateTimeField(null=True)),
                ('date_remitted', models.DateTimeField(null=True)),
                ('date_received', models.DateTimeField(null=True)),
                ('amount_remitted', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('received_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('SUBMITTED', 'Submitted'), ('APPROVED', 'Approved'), ('REMITTED', 'Remitted'), ('RECEIVED', 'Received')], default='CREATED', max_length=9)),
                ('period', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='timesheets.usertimesheetperiod')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice')),
            ],
        ),
    ]