# Generated by Django 2.1 on 2020-01-12 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
