# Generated by Django 4.2.4 on 2024-11-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skylineFacade', '0004_remove_majorprojects_image_projectimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='majorprojects',
            name='featured_image',
            field=models.ImageField(null=True, upload_to='project_images/'),
        ),
    ]
