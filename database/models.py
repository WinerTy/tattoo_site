from django.db import models
from site_setting.models import Salon, SocialAccountIcon
from UserAuth.models import CustomUser


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


class TattooType(models.Model):
    name = models.CharField(max_length=30, verbose_name="Тип тату")

    class Meta:
        verbose_name = "Тип тату"
        verbose_name_plural = "Типы тату"

    def __str__(self):
        return self.name


class Master(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        blank=True,
        unique=True,
        related_name="user_master",
    )
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name="Салон")
    photo = models.ImageField(upload_to="MastersPhoto/", verbose_name="Фотография")
    name = models.CharField(max_length=20, verbose_name="Имя")
    description = models.TextField(blank=True, verbose_name="Описание")
    works = models.ManyToManyField(Works, blank=True, verbose_name="Работы мастера")
    experience = models.PositiveIntegerField(default=0, verbose_name="Стаж работы")
    tattoo_type = models.ManyToManyField(
        TattooType, blank=True, verbose_name="Типы тату"
    )
    education = models.CharField(max_length=100, blank=True, verbose_name="Образование")
    is_active = models.BooleanField(default=True, verbose_name="Отоброжать")

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"

    def __str__(self):
        return self.name


class Session(models.Model):
    DAYS_OF_WEEK = (
        ("Понедельник", "Понедельник"),
        ("Вторник", "Вторник"),
        ("Среда", "Среда"),
        ("Четверг", "Четверг"),
        ("Пятница", "Пятница"),
        ("Суббота", "Суббота"),
        ("Воскресенье", "Воскресенье"),
    )

    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер")
    day_of_week = models.CharField(
        max_length=20, choices=DAYS_OF_WEEK, verbose_name="День недели"
    )
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    is_active = models.BooleanField(default=True, verbose_name="Актуальный")

    class Meta:
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеансы"

    def __str__(self):
        return f"Сеанс {self.master.name} на {self.get_day_of_week_display()}"


class SocialAccount(models.Model):
    master = models.ForeignKey(
        Master,
        verbose_name="Мастер",
        on_delete=models.CASCADE,
        related_name="social_account",
    )
    icon = models.OneToOneField(SocialAccountIcon, on_delete=models.CASCADE)
    link = models.URLField(verbose_name="Ссылка")

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return self.link


class Note(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.client_email
