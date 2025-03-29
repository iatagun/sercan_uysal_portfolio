from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class ContactInfo(models.Model):
    office_address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"İletişim Bilgileri"

    class Meta:
        verbose_name = "İletişim Bilgisi"
        verbose_name_plural = "İletişim Bilgileri"

class SocialLink(models.Model):
    platform_name = models.CharField(max_length=50)
    url = models.URLField(max_length=250)
    icon_class = models.CharField(max_length=50, help_text='İkon sınıfı örn: ri-facebook-circle-fill')

    def __str__(self):
        return self.platform_name

    class Meta:
        verbose_name = "Sosyal Medya Linki"
        verbose_name_plural = "Sosyal Medya Linkleri"

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

    class Meta:
        verbose_name = "İletişim Formu Mesajı"
        verbose_name_plural = "İletişim Formu Mesajları"
        ordering = ['-created_at']
    
class About(models.Model):
    title = models.CharField(max_length=100, default='Hakkımda')
    name = models.CharField(max_length=100, default='Sercan Uysal')
    short_description = models.TextField(help_text='Kısa ve öz bir giriş cümlesi.', blank=True)
    detailed_description = models.TextField(help_text='Ayrıntılı hakkımda bilgisi.')
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    tools = models.CharField(max_length=255, help_text='Kullanılan araçları virgülle ayırarak yazın.', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hakkımda'
        verbose_name_plural = 'Hakkımda Bilgileri'

    def __str__(self):
        return self.name
    
class SkillSection(models.Model):
    title = models.CharField(max_length=100, default='My Skills')
    subtitle = models.CharField(max_length=150, default='Every Day is a New Challenge')
    description = models.TextField()
    additional_description = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=50, default='Contact Me')
    button_link = models.CharField(max_length=100, default='#contact')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill Bölümü'
        verbose_name_plural = 'Skill Bölümleri'

    def __str__(self):
        return self.title

class Skill(models.Model):
    section = models.ForeignKey(SkillSection, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    proficiency_percentage = models.PositiveIntegerField(default=50, help_text='Yüzde olarak beceri seviyesi (0-100)')

    class Meta:
        verbose_name = 'Beceri'
        verbose_name_plural = 'Beceriler'

    def __str__(self):
        return f"{self.name} - {self.proficiency_percentage}%"
    
    class ProjectCategory(models.Model):
        name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Proje Kategorisi"
        verbose_name_plural = "Proje Kategorileri"

    def __str__(self):
        return self.name

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Proje Kategorisi"
        verbose_name_plural = "Proje Kategorileri"

    def __str__(self):
        return self.name

class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(max_length=500, blank=True, null=True, help_text='Opsiyonel proje bağlantısı (Youtube veya web sitesi).')
    is_video = models.BooleanField(default=False, help_text='Eğer link video ise bu alanı işaretleyin.')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"

    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    image = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name="Kapak Resmi")
    summary = models.TextField(max_length=400, verbose_name="Özet")
    content = models.TextField(verbose_name="İçerik")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")
    is_published = models.BooleanField(default=True, verbose_name="Yayınlansın mı?")

    class Meta:
        verbose_name = "Blog Yazısı"
        verbose_name_plural = "Blog Yazıları"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
                
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})
    
class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"