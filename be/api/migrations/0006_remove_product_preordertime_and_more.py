# Generated by Django 4.1.5 on 2023-04-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_cart_deleted_at_remove_cart_is_deleted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='preorderTime',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='preOrderTime',
        ),
        migrations.AddField(
            model_name='product',
            name='readyAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='readyAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]