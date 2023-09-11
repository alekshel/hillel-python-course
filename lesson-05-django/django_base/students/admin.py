from django.contrib import admin

# Register your models here.
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)