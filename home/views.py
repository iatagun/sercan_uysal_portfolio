from django.shortcuts import render, HttpResponse, redirect
from .models import About
from django.shortcuts import render, get_object_or_404
from .models import SkillSection, Skill, ProjectCategory, Project
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactInfo, SocialLink, ContactMessage
# Create your views here.


def home(request):
    about_info = About.objects.latest('updated_at')
    title = about_info.title
    name = about_info.name
    detailed_description = about_info.detailed_description
    image = about_info.image
    skill_section = get_object_or_404(SkillSection)
    categories = ProjectCategory.objects.prefetch_related('projects').all()
    last_three_projects = Project.objects.order_by('-id')[:3]
    categories_img = Project.image
    contact_info = ContactInfo.objects.first()
    social_links = SocialLink.objects.all()


    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')

        if full_name and email and subject and message_text:
            # Email Gönder
            send_mail(
                subject=f"{subject} - {full_name}",
                message=f"Sender: {full_name}\nEmail: {email}\n\nMessage:\n{message_text}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],  # gönderdiğin mailin adresine gelir
                fail_silently=False,
            )
            messages.success(request, 'We have received your email, we will get back to you soon!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields and try again.')

    context = {
        'about_info': about_info,
        'title': title,
        'name': name,
        'detailed_description': detailed_description,
        'image': image,
        'skill_section': skill_section,
        'categories': categories,
        'categories_img': categories_img,
        'contact_info': contact_info,
        'social_links': social_links,
        'projects': last_three_projects
    }
    return render(request, 'index.html', context)


def project(request):
    return render(request, 'project.html')

def about(request):
    about_info = About.objects.latest('updated_at')
    title = about_info.title
    name = about_info.name
    detailed_description = about_info.detailed_description
    image = about_info.image
    skill_section = get_object_or_404(SkillSection)
    categories = ProjectCategory.objects.prefetch_related('projects').all()
    last_three_projects = Project.objects.order_by('-id')[:3]
    categories_img = Project.image
    contact_info = ContactInfo.objects.first()
    social_links = SocialLink.objects.all()

    context = {
        'about_info': about_info,
        'title': title,
        'name': name,
        'detailed_description': detailed_description,
        'image': image,
        'skill_section': skill_section,
        'categories': categories,
        'categories_img': categories_img,
        'contact_info': contact_info,
        'social_links': social_links,
        'projects': last_three_projects
    }

    return render(request, 'about.html', context)

def service(request):
    return render(request, 'service.html')

def projects(request):
    return render(request, 'projects.html')

def blog(request):
    return render(request, 'blog.html')



def contact(request):
    return render(request, 'index.html')

