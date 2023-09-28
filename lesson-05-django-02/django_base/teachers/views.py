from django.http import JsonResponse

from teachers.models import Teacher


def get_all(request):
    teachers = list()
    for teacher in Teacher.objects.all():
        teachers.append(
            {
                "id": teacher.id,
                "first_name": teacher.first_name,
                "last_name": teacher.last_name,
                "subject": teacher.subject,
            }
        )

    return JsonResponse({"teachers": teachers})
