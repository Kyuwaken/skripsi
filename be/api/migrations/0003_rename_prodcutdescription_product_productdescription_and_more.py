# Generated by Django 4.1.5 on 2023-03-22 07:53

import api.models.product_image_model
import auto_prefetch
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_productphoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prodcutDescription',
            new_name='productDescription',
        ),
        migrations.RemoveField(
            model_name='product',
            name='productPhoto',
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('productPhoto', models.ImageField(null=True, upload_to=api.models.product_image_model.file_path)),
                ('created_by', auto_prefetch.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_fk_created', to='api.user')),
                ('product', auto_prefetch.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('updated_by', auto_prefetch.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_fk_updated', to='api.user')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]