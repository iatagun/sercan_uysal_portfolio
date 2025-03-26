from django.shortcuts import render, HttpResponse
from .models import About, Contact
from django.shortcuts import render, get_object_or_404
from .models import SkillSection, Skill, ProjectCategory, Project

# Create your views here.


def home(request):
    about_info = About.objects.latest('updated_at')
    title = about_info.title
    name = about_info.name
    detailed_description = about_info.detailed_description
    image = about_info.image
    skill_section = get_object_or_404(SkillSection)
    categories = ProjectCategory.objects.prefetch_related('projects').all()
    categories_img = Project.image

    context = {
        'about_info': about_info,
        'title': title,
        'name': name,
        'detailed_description': detailed_description,
        'image': image,
        'skill_section': skill_section,
        'categories': categories,
        'categories_img': categories_img
    }
    return render(request, 'index.html', context)


def project(request):
    return render(request, 'project.html')

def about(request):
    # En son güncellenmiş About nesnesini al
    about_info = About.objects.latest('updated_at')
    title = about_info.title
    name = about_info.name

    context = {
        'about_info': about_info,
        'title': title,
        'name': name
    }

    return render(request, 'about.html', context)

def service(request):
    return render(request, 'service.html')

def project(request):
    return render(request, 'project.html')

def blog(request):
    return render(request, 'blog.html')



def contact(request):
    return render(request, 'index.html')

