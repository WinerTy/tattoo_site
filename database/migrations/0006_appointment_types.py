# Generated by Django 5.0.6 on 2024-05-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_appointment_client_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='types',
            field=models.ManyToManyField(blank=True, to='database.tattootype', verbose_name='Интересующие типы тату'),
        ),
    ]
