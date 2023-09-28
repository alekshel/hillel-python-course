from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField("Ім'я", max_length=255, default="")
    last_name = models.CharField("Прізвище", max_length=255, default="")
    subject = models.CharField("Предмет", max_length=255, default="")

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.subject})"

    class Meta:
        verbose_name = "Вчитель"
        verbose_name_plural = "Вчителі"
