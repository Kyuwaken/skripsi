import json
from django.core.management.base import BaseCommand
from api.models import Category, User, Role, MasterStatus, PaymentMethod, PaymentType, Country
from api.utils.pycrypto import encrypt_data


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
            data['password'] = encrypt_data(data['password'])
            User.objects.get_or_create(
                name=data['name'], defaults=data)
        self.comment("Seeding User")
    
    def seed_master_status(self):
        with open('api/json/master_status.json') as f:
            data_list = json.load(f)

        for data in data_list:
            MasterStatus.objects.get_or_create(name=data['name'], defaults=data)
        self.comment("Seeding Master Status")

    def seed_payment_method(self):
        with open('api/json/payment_method.json') as f:
            data_list = json.load(f)

        for data in data_list:
            PaymentMethod.objects.get_or_create(name=data['name'], defaults=data)
        self.comment("Seeding Payment Method")
    
    def seed_payment_type(self):
        with open('api/json/payment_type.json') as f:
            data_list = json.load(f)

        for data in data_list:
            PaymentType.objects.get_or_create(name=data['name'], defaults=data)
        self.comment("Seeding Payment Type")
    
    def seed_country(self):
        with open('api/json/country.json') as f:
            data_list = json.load(f)

        for data in data_list:
            Country.objects.get_or_create(name=data['name'], defaults=data)
        self.comment("Seeding Country")

    def comment(self, comment):
        self.stdout.write(self.style.HTTP_SUCCESS('%s... ' %
                          comment)+self.style.SUCCESS('OK'))

    def handle(self, *args, **options):
        self.seed_role()
        self.seed_category()
        self.seed_user()
        self.seed_master_status()
        self.seed_payment_method()
        self.seed_payment_type()
        self.seed_country()

