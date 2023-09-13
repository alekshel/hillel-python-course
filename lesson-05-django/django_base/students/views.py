from django.http import JsonResponse
import random

from faker import Faker

from .models import Student


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    

def create_student():
    fake = Faker('uk')

    student = Student.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=random.randint(16, 30)
    )

    return {
        "id": student.id,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "age": student.age
    }


def generate_student(request):
    student = create_student()
    return JsonResponse(student)


def generate_students(request):
    count = request.GET.get('count')
    if not count or not is_int(count):
        return JsonResponse({
            "error": "Параметр count не корректний"
        })
    
    count = int(count)

    if count <= 0 or count > 100:
        return JsonResponse({
            "error": "Параметр count пивинен бути більше 0 та менше або дорівнювати 100"
        })
    
    students = list()
    for i in range(count):
        students.append(
            create_student()
        )

    return JsonResponse({
        "students": students
    })
