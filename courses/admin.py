from django.contrib import admin
from .models import Course, Subject, Module

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug' : ('title',)}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','subject', 'created']
    prepopulated_fields = {'slug' : ('title',)}
    inlines = [ModuleInline]
