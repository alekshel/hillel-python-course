from django.contrib import admin

# Register your models here.
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Teacher, TeacherAdmin)