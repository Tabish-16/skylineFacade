# Generated by Django 4.2.4 on 2024-11-21 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skylineFacade', '0011_alter_services_shor_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='shor_description',
            new_name='short_description',
        ),
    ]
