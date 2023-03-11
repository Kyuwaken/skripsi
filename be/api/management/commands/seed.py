import json
from django.core.management.base import BaseCommand
from api.models import Category, User, Role


class Command(BaseCommand):

    def seed_category(self):
        with open('api/json/category.json') as f:
            data_list = json.load(f)

        for data in data_list:
            Category.objects.get_or_create(name=data['name'], defaults=data)
        self.comment("Seeding Category")

    def seed_role(self):
        with open('api/json/role.json') as f:
            data_list = json.load(f)

        for data in data_list:
            Role.objects.get_or_create(name=data['name'], defaults=data)
        self.comment("Seeding Role")

    def seed_user(self):
        with open('api/json/user.json') as f:
            data_list = json.load(f)

        for data in data_list:
            role = Role.objects.get(pk=data['role'])
            data['role'] = role
            User.objects.get_or_create(
                name=data['name'], defaults=data)
        self.comment("Seeding User")

    def comment(self, comment):
        self.stdout.write(self.style.HTTP_SUCCESS('%s... ' %
                          comment)+self.style.SUCCESS('OK'))

    def handle(self, *args, **options):
        self.seed_role()
        self.seed_category()
        self.seed_user()
