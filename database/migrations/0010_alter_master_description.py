# Generated by Django 5.0.6 on 2024-06-04 14:21

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_master_short_description_alter_master_min_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Описание'),
        ),
    ]