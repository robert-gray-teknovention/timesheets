# Generated by Django 4.1.6 on 2023-04-28 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_alter_serialpart_parent_serial_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serialpart',
            name='man_serial_number',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='serialpart',
            name='type',
            field=models.CharField(choices=[('STANDARD', 'Standard'), ('ASSEMBLY', 'Assembly'), ('EQUIPMENTEquipment', 'Equipment')], default='STANDARD', max_length=20),
        ),
    ]
