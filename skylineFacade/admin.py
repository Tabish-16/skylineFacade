from django.contrib import admin
from skylineFacade.models import *


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Number of extra forms to display

class MajorProjectsAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    inlines = [ProjectImageInline]

admin.site.register(MajorProjects, MajorProjectsAdmin)



class ServicesImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1  # Number of extra forms to display

class ServicesAdmin(admin.ModelAdmin):
    inlines = [ServicesImageInline]

admin.site.register(Services, ServicesAdmin)



class BlogPostAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Health_safety)
admin.site.register(Contactus)


class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)
admin.site.register(Products,ProductAdmin)