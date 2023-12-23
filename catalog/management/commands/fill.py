from django.core.management.base import BaseCommand

from catalog.models import Category


# from cata4


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()

        Category.objects.create(name='Категория 1', description='Описание категории 1')
        Category.objects.create(name='Категория 2', description='Описание категории 2')
        Category.objects.create(name='Категория 3', description='Описание категории 3')

        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены в базу данных'))