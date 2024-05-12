from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    longitude = models.CharField(max_length=100, verbose_name="Долгота")
    latitude = models.CharField(max_length=100, verbose_name="Широта")