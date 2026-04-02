from django.contrib import admin
from .models import Skills

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['name','proficiency']
    search_fields = ['name','proficiency']

# Register your models here.
