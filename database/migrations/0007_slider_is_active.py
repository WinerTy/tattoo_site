# Generated by Django 5.0.6 on 2024-05-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_slider_alter_socialaccount_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Отоброжать'),
        ),
    ]