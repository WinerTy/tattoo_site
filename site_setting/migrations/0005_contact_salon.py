# Generated by Django 5.0.6 on 2024-05-17 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0004_salon_remove_contact_address_remove_contact_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='salon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='site_setting.salon'),
            preserve_default=False,
        ),
    ]