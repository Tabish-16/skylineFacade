# Generated by Django 4.2.4 on 2024-11-18 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skylineFacade', '0002_majorprojects_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='majorprojects',
            name='facede_materials',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='majorprojects',
            name='scope',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
