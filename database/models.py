from django.db import models
from site_setting.models import Salon


class Slider(models.Model):
    photo = models.ImageField(upload_to="Slider/", verbose_name="Картинка")
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    is_active = models.BooleanField(default=True, verbose_name="Отоброжать")

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"

    def __str__(self):
        return self.title


class Works(models.Model):
    photo = models.ImageField(upload_to="WorksPhoto/", verbose_name="Фотография")
    name = models.CharField(max_length=30, verbose_name="Название")
    type = models.CharField(max_length=30, verbose_name="Тип тату")

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

    def __str__(self):
        return self.name


class Master(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="MastersPhoto/",
                              verbose_name="Фотография")
    name = models.CharField(max_length=20, verbose_name="Имя")
    description = models.TextField(blank=True, verbose_name="Описание")
    works = models.ManyToManyField(Works, blank=True, verbose_name="Работы мастера")
    experience = models.PositiveIntegerField(default=0, verbose_name="Стаж работы")
    tattoo_type = models.CharField(max_length=50, verbose_name="Тип татуировок")
    is_active = models.BooleanField(default=True, verbose_name="Отоброжать")

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"

    def __str__(self):
        return self.name


class SocialAccount(models.Model):
    master = models.ForeignKey(Master, verbose_name="Мастер", on_delete=models.CASCADE, related_name='social_account')
    icon = models.ImageField(upload_to="MastersSocial/", verbose_name="Иконка")
    link = models.CharField(max_length=150, verbose_name="Ссылка")

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return self.link


class Note(models.Model):
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.client_email
