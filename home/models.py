from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=40)
    


    def __str__(self):
        return self.name
    
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