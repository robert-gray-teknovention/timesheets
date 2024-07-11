# Generated by Django 4.1.6 on 2023-03-04 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0014_rename_email_organization_mailer_email'),
        ('employee', '0009_alter_timesheetuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheetuser',
            name='org_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='managers', to='organizations.organization'),
        ),
    ]