# Generated by Django 4.1.5 on 2023-04-22 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='productPhoto',
            new_name='image',
        ),
    ]
