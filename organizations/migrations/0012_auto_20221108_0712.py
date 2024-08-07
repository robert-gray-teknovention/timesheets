# Generated by Django 3.2.16 on 2022-11-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0011_alter_periodtype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='timezone',
            field=models.CharField(blank=True, choices=[['ch', 'Chicago'], ['ny', 'New York'], ['la', 'Los Angeles']], default='America/Los_Angeles', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='periodtype',
            name='seed_date',
            field=models.DateTimeField(help_text='This field is only used if name is weekly or biweekly'),
        ),
    ]
