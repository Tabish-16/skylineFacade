# Generated by Django 4.2.4 on 2024-11-21 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skylineFacade', '0010_services_shor_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='shor_description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
