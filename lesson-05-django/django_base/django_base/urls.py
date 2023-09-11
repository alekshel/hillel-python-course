"""
URL configuration for django_base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from students import views as views_students
from teachers import views as views_teachers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-student/', views_students.generate_student, name='generate_student'),
    path('generate-students/', views_students.generate_students, name='generate_students'),
    path('teachers/', views_teachers.get_all, name='teachers'),
]
