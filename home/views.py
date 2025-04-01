from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import About, Contact
from django.shortcuts import render, get_object_or_404
from .models import SkillSection, Skill, ProjectCategory, Project
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactInfo, SocialLink, ContactMessage
from .models import BlogPost
from django.http import FileResponse
from .models import PDFDocument
# Create your views here.


def home(request):
    about_info = About.objects.latest('updated_at')
    title = about_info.title
    name = about_info.name
    detailed_description = about_info.detailed_description
    image = about_info.image
    skill_section = SkillSection.objects.first()
    categories = ProjectCategory.objects.prefetch_related('projects').all()
    last_three_projects = Project.objects.order_by('-id')[:3]
    categories_img = Project.image
    contact_info = ContactInfo.objects.first()
    social_links = SocialLink.objects.all()
    beceri = SkillSection.objects.all()[1]


    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Form verilerini Contact modeline kaydet
        Contact.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, "Mesajınız başarıyla gönderildi!")

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
        'projects': last_three_projects,
        'beceri': beceri
    }
    return render(request, 'index.html', context)


def project(request):
    about_info = About.objects.latest('updated_at')
    title = about_info.title
    name = about_info.name
    detailed_description = about_info.detailed_description
    image = about_info.image
    skill_section = SkillSection.objects.first()
    categories = ProjectCategory.objects.prefetch_related('projects').all()
    last_three_projects = Project.objects.order_by('-id')
    categories_img = Project.image
    contact_info = ContactInfo.objects.first()
    social_links = SocialLink.objects.all()
    blog_posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')[:1]

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
        'projects': last_three_projects,
        'blog_posts': blog_posts,
    }
    return render(request, 'project.html', context)

def about(request):
    about_info = About.objects.latest('updated_at')
    title = about_info.title
    name = about_info.name
    detailed_description = about_info.detailed_description
    image = about_info.image
    skill_section = SkillSection.objects.first()
    categories = ProjectCategory.objects.prefetch_related('projects').all()
    last_three_projects = Project.objects.order_by('-id')[:3]
    categories_img = Project.image
    contact_info = ContactInfo.objects.first()
    social_links = SocialLink.objects.all()
    blog_posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')[:1]
    print(SkillSection.objects.all()[1])
    beceri = SkillSection.objects.all()[1]

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
        'projects': last_three_projects,
        'blog_posts': blog_posts,
        'beceri' : beceri
    }

    return render(request, 'about.html', context)

def service(request):
    return render(request, 'service.html')

def projects(request):
    return render(request, 'projects.html')

def twod(request):
    twod = Project.objects.filter(category__name__iexact='2d').order_by('-id')

    context = {
        'twod': twod,
    }

    return render(request, '2d.html', context)

def threed(request):
    threed = Project.objects.filter(category__name__iexact='3d').order_by('-id')

    context = {
        'threed': threed,
    }

    return render(request, '3d.html', context)

def blog(request):
    return render(request, 'blog.html')

def get_absolute_url(self):
    return reverse("blog_detail", kwargs={"slug": self.slug})

def contact(request):
    about_info = About.objects.latest('updated_at')
    title = about_info.title
    name = about_info.name
    detailed_description = about_info.detailed_description
    image = about_info.image
    skill_section = SkillSection.objects.first()
    categories = ProjectCategory.objects.prefetch_related('projects').all()
    last_three_projects = Project.objects.order_by('-id')[:3]
    categories_img = Project.image
    contact_info = ContactInfo.objects.first()
    social_links = SocialLink.objects.all()
    blog_posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')[:1]

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
        'projects': last_three_projects,
        'blog_posts': blog_posts,
    }
    return render(request, 'contact.html', context)

def download_pdf(request, pk):
    """
    Verilen pk'ya sahip PDFDocument nesnesini bularak, dosyayı indirme olarak sunar.
    """
    pdf_document = get_object_or_404(PDFDocument, pk=pk)
    if pdf_document.pdf_file:
        return FileResponse(
            pdf_document.pdf_file.open('rb'),
            as_attachment=True,
            filename=f"{pdf_document.title}.pdf"
        )
    else:
        return HttpResponse("Dosya bulunamadı.", status=404)

def pdf_download_page(request, pk):
    pdf_document = get_object_or_404(PDFDocument, pk=pk)
    return render(request, 'pdf_download_page.html', {'pdf_document': pdf_document})
