"""Django_Portfilio_MohammadBurhan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('project', views.project, name='project'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('project', views.project, name='project'),
    path('projects', views.project, name='projects'),
    path('blog', views.blog, name='blog'),
    path('2d', views.twod, name='2d'),
    path('3d', views.threed, name='3d'),
    
    path('download/<int:pk>/', views.download_pdf, name='download_pdf'),
    path('pdf/<int:pk>/', views.pdf_download_page, name='pdf_download_page'),

]
