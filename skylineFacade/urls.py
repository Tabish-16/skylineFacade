"""
URL configuration for AryanCranes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, re_path
from django.views import static
from django.views.static import serve 
from django.conf.urls.static import static

from skylineFacade import settings, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('about-us/', views.aboutus,name='about-us'),
    path('projects/', views.projects,name='projects'),
    path('projectsDetails/<slug:slug>/', views.projectsDetails, name='projectsDetails'),
    path('careers/', views.careers,name='careers'),
    path('contact-us/', views.contact_us,name='contact-us'),
    path('services/', views.services,name='services'),
    path('services-details/<slug:slug>/', views.services_details,name='services-details'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog-details/<slug:slug>/', views.blogs_details, name='blog-details'),
    path('Facade_Engineering_Services/', views.Facade_Engineering_Services, name='Facade_Engineering_Services'),
    path('Facade_Design_Consultancy/', views.Facade_Design_Consultancy, name='Facade_Design_Consultancy'),
    path('products/', views.products, name='products'),
    path('upvcWindows/', views.upvcWindows, name='upvcWindows'),
    path('Aluminum-Doors-Windows/', views.Aluminum_Doors_Windows, name='Aluminum_Doors_Windows'),
    path('facade_system/', views.facade_system, name='facade_system'),
    path('point_fixed/', views.point_fixed, name='point_fixed'),
    path('louvers/', views.louvers, name='louvers'),
    path('balustrade/', views.balustrade, name='balustrade'),
    path('internal-glass-partition/', views.glass_partition, name='glass_partition'),
    path('skylight-steel-structure/', views.street_structure, name='street_structure'),
    
    
    # path('quality-policy/', views.qualitypolicy,name='quality-policy'),
    # path('mission&vission/', views.mission_vission,name='mission&vission'),
    # path('blogs/', views.blogs, name='blogs'),
    # path('contactus/', views.contactus, name='contactus'),
    # path('health-safety/', views.health_safety, name='health-safety'),
    # path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    # # path('projects/<slug:slug>/', views.projects, name='projects'),
    # path('major-projects/', views.majorProjects, name='major-projects'),
    # path('projectsDetails/<slug:slug>/', views.projectsDetails, name='projectsDetails'),
    # path('all_cranes/', views.cranes, name='all_cranes'),
    # path('our_clients/', views.our_clients, name='our_clients'),

    # re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    
    ] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)