# Generated by Django 4.2.4 on 2024-11-15 09:17

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('content', tinymce.models.HTMLField()),
                ('author', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('meta_description', models.CharField(blank=True, help_text='A brief summary of the content for search engines', max_length=160, null=True)),
                ('meta_keywords', models.CharField(blank=True, help_text='Comma-separated list of keywords or topics related to the content', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Health_safety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', tinymce.models.HTMLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MajorProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('description', tinymce.models.HTMLField(null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
