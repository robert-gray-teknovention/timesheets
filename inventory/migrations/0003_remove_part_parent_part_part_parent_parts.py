# Generated by Django 4.1.6 on 2023-04-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_serialpart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='parent_part',
        ),
        migrations.AddField(
            model_name='part',
            name='parent_parts',
            field=models.ManyToManyField(blank=True, related_name='child_parts', to='inventory.part'),
        ),
    ]
