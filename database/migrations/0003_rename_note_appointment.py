# Generated by Django 5.0.6 on 2024-05-29 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_master_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Appointment',
        ),
    ]
