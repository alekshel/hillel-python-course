import sys

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from teachers.models import Teacher

fake = Faker("uk")


class Command(BaseCommand):
    help = "Add specified number of teachers"

    def add_arguments(self, parser):
        parser.add_argument("-n", "--number", type=int, default=100)

    def handle(self, *args, **options):
        number = options["number"]
        if number < 1:
            self.stdout.write(self.style.ERROR("Number must be greater than 0"))
            sys.exit(1)

        for i in range(number):
            teacher = Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                subject=fake.job(),
            )

            self.stdout.write(
                self.style.SUCCESS('Successfully added teacher "%s"' % teacher.id)
            )
