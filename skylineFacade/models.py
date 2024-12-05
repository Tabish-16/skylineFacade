from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from tinymce.models import HTMLField


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200,null=True)
    short_description = models.CharField(max_length=300,null=True)
    content = HTMLField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    img = models.ImageField(null=True)
    meta_description = models.CharField(max_length=160, null=True, blank=True,help_text="A brief summary of the content for search engines")
    meta_keywords = models.CharField(max_length=255, null=True, blank=True,help_text="Comma-separated list of keywords or topics related to the content")

    def save(self, *args, **kwargs):
        if not self.slug:
            print(f"Generating slug for title: {self.title}")
            self.slug = slugify(self.title)
            counter = 1
            unique_slug = self.slug
            while BlogPost.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug
            print(f"Generated slug: {self.slug}")
        else:
            print(f"Slug already exists: {self.slug}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
class MajorProjects(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    project = models.CharField(max_length=1000, blank=True, null=True)
    scope = models.CharField(max_length=1000, blank=True, null=True)
    facede_materials = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=200, null=True)
    description = HTMLField(null=True)
    featured_image = models.ImageField(upload_to='project_images/',null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            counter = 1
            unique_slug = self.slug
            while MajorProjects.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(MajorProjects, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project.title}"
    
class Health_safety(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    description = HTMLField(null=True)    
    
    def __str__(self):
        return self.title
    
class Contactus(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name    


class Services(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=200, null=True)
    featured_image = models.ImageField(upload_to='project_images/',null=True)
    short_description = models.CharField(max_length=500,null=True,blank=False)
    description = HTMLField(null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            counter = 1
            unique_slug = self.slug
            while Services.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ServiceImage(models.Model):
    project = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for {self.project.title}"    
    
    
    
class Products(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=200, null=True)
    featured_image = models.ImageField(upload_to='product_images/',null=True)
    short_description = models.CharField(max_length=500,null=True,blank=False)
    description = HTMLField(null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            counter = 1
            unique_slug = self.slug
            while Products.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    