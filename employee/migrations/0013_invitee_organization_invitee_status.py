# Generated by Django 4.1.6 on 2023-07-06 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0014_rename_email_organization_mailer_email'),
        ('employee', '0012_invitee'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitee',
            name='organization',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.organization'),
        ),
        migrations.AddField(
            model_name='invitee',
            name='status',
            field=models.CharField(choices=[('INVITED', 'Invited'), ('REGISTERED', 'Registered'), ('ACTIVATED', 'Activated')], default='INVITED', max_length=10),
        ),
    ]
