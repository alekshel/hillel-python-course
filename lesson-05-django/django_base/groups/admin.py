from django.contrib import admin

# Register your models here.
from .models import Group

class GroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(Group, GroupAdmin)