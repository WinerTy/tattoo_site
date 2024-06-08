import os
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Slider(models.Model):
    photo = models.ImageField(upload_to="Site/Slider/", verbose_name="Картинка")
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    is_active = models.BooleanField(default=True, verbose_name="Отоброжать")

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"

    def __str__(self):
        return self.title


class Salon(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название салона")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    longitude = models.CharField(max_length=100, verbose_name="Долгота")
    latitude = models.CharField(max_length=100, verbose_name="Широта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Салон"
        verbose_name_plural = "Салоны"

    def __str__(self):
        return self.name

    def get_session_data(self):
        data = {
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "name": self.name,
            "pk": self.pk,
        }
        return data


class SalonSocial(models.Model):
    SOCIAL = (
        ("vk", "VK"),
        ("telegram", "Telegram"),
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("youtube", "Youtube"),
        ("twitter", "Twitter"),
        ("whatsapp", "Whatsapp"),
    )
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    social = models.CharField(
        max_length=20, choices=SOCIAL, verbose_name="Социальная сеть"
    )
    link = models.URLField(verbose_name="Ссылка")

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return self.social


class Contact(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта")


class AboutBlock(models.Model):
    image = models.ImageField(upload_to="Site/AboutImages/", verbose_name="Картинка")
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    short_description = models.TextField(
        verbose_name="Краткое описание",
        help_text="Текст отоброжаемый на главной странице",
    )
    description = CKEditor5Field("Описание", config_name="extends")

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self):
        return self.title


class SocialAccountIcon(models.Model):
    icon = models.ImageField(upload_to="Site/SocialIcons/", verbose_name="Иконка")

    class Meta:
        verbose_name = "Социальная сеть иконка"
        verbose_name_plural = "Социальные сети иконки"

    def __str__(self):
        return os.path.basename(self.icon.path)
