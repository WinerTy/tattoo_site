# Generated by Django 5.0.6 on 2024-06-08 10:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_delete_slider'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_email', models.EmailField(max_length=254)),
                ('client_phone', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client_name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False, help_text='Мастер дал ответ клиенту', verbose_name='Ответил')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.master')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.session')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
        migrations.DeleteModel(
            name='AppointmentV2',
        ),
    ]
