# Generated by Django 4.2.4 on 2024-11-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skylineFacade', '0015_blogpost_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='short_description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
