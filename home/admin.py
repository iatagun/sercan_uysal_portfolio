from django.contrib import admin
#from home.models import Home
from home.models import About
from .models import Contact, SkillSection, Skill
from .models import BlogPost
from .models import ProjectCategory, Project, PDFDocument

from .models import ContactInfo, SocialLink, ContactMessage

# Register your models here.

#admin.site.register(Home)
admin.site.register(About)

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

@admin.register(SkillSection)
class SkillSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'updated_at')
    inlines = [SkillInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency_percentage', 'section')
    list_filter = ('section',)
    search_fields = ('name',)

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_video', 'updated_at')
    list_filter = ('category', 'is_video')
    search_fields = ('title',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['office_address', 'phone_number', 'email']

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform_name', 'url']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'created_at']
    search_fields = ['full_name', 'email', 'subject']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'summary', 'content')

admin.register(Contact)


from django.utils.html import format_html
@admin.register(PDFDocument)
class PDFDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'download_link')
    readonly_fields = ('uploaded_at', 'download_link')

    def download_link(self, obj):
        """
        Eğer PDF dosyası mevcutsa, indirme linki oluşturur.
        """
        if obj.pdf_file:
            return format_html('<a href="{}" target="_blank">PDF İndir</a>', obj.pdf_file.url)
        return "Dosya yok"
    download_link.short_description = "PDF İndir"