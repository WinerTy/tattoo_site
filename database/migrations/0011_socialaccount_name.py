# Generated by Django 5.0.6 on 2024-06-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_alter_master_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialaccount',
            name='name',
            field=models.CharField(default=1, help_text='Текст который будет отображен вместо ссылки', max_length=20, verbose_name='Название'),
            preserve_default=False,
        ),
    ]