from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField('Назва групи', max_length=255, default='')
    students_count = models.IntegerField('Кількість студентів', default='')

    def __str__(self):
        return f"{self.name} ({self.students_count})"

    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'


from django.db.models.signals import post_migrate
from django.dispatch import receiver

import random
from faker import Faker
fake = Faker('uk')

@receiver(post_migrate)
def add_initial_data(sender, **kwargs):
    if sender.name == 'groups' and Group.objects.count() == 0:
        for i in range(5):
            group_name = f"{fake.random_letter().upper()} - {random.randint(1, 5)}"
            Group.objects.create(
                name=group_name,
                students_count=random.randint(18, 32)
            )