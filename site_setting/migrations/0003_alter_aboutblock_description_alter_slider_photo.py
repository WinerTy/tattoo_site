# Generated by Django 5.0.6 on 2024-06-08 07:30

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0002_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutblock',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='photo',
            field=models.ImageField(upload_to='Site/Slider/', verbose_name='Картинка'),
        ),
    ]
