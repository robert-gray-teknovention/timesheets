# Generated by Django 4.1.6 on 2023-02-14 15:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=75)),
                ('recipients', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=75), size=50), size=50)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=2500)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
