# Generated by Django 3.2.16 on 2022-11-05 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_alter_organization_street2'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyPeriodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SemiMonthlyPeriodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
