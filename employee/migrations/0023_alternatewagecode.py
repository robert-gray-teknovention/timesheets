# Generated by Django 4.1.6 on 2023-10-14 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0022_alter_invitee_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlternateWageCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourly_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('description', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.timesheetuser')),
            ],
        ),
    ]
