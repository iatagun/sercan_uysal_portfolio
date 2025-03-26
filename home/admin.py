from django.contrib import admin
#from home.models import Home
from home.models import Contact, About
from .models import SkillSection, Skill

from .models import ProjectCategory, Project

# Register your models here.

#admin.site.register(Home)
admin.site.register(Contact)
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

