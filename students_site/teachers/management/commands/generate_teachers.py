from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Teacher

fake = Faker()


class Command(BaseCommand):
    help = "Add the specified number of teachers to rhe database"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=100)

    def handle(self, *args, **options):
        number = options["number"]
        if number < 1:
            self.stdout.write(self.style.ERROR("Enter a number greater than 0!!!"))
        for i in range(number):
            teacher = Teacher.objects.create(
                first_name=fake.first_name(),
                surname=fake.last_name(),
                birth_day=fake.date(),
                subject=fake.random_element(
                    elements=(
                        "English",
                        "math",
                        "physics",
                        "reading",
                        "history",
                        "biology",
                    )
                ),
            )

            self.stdout.write(
                self.style.SUCCESS('Successfully added teacher "%s"' % teacher.id)
            )
