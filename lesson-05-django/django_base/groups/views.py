from django.http import JsonResponse

# Create your views here.
from .models import Group

def get_all(request):
    groups = list()
    for group in Group.objects.all():
        groups.append({
            "id": group.id,
            "name": group.name,
            "students_count": group.students_count
        })

    return JsonResponse({
        "groups": groups
    })
