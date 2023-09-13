from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField('Ім\'я', max_length=255, default='')
    last_name = models.CharField('Прізвище', max_length=255, default='')
    subject = models.CharField('Предмет', max_length=255, default='')

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.subject})"

    class Meta:
        verbose_name = 'Викладач'
        verbose_name_plural = 'Викладачі'


from django.db.models.signals import post_migrate
from django.dispatch import receiver

from faker import Faker
fake = Faker('uk')
SUBJECT_NAMES = (
    'Математика',
    'Фізика',
    'Фіз. культура',
    'Астрономія',
    'Українська мова'
)

@receiver(post_migrate)
def add_initial_data(sender, **kwargs):
    if sender.name == 'teachers':
        for i in range(5):
            Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                subject=fake.random_element(elements=SUBJECT_NAMES)
            )