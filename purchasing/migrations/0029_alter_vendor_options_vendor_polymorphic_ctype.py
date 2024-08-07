# Generated by Django 4.1.6 on 2023-04-28 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('purchasing', '0028_alter_purchaseorderitem_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendor',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AddField(
            model_name='vendor',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
    ]
