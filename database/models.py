from django.db import models
from site_setting.models import Salon, SocialAccountIcon
from UserAuth.models import CustomUser
from django_ckeditor_5.fields import CKEditor5Field


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
        null=True,
    )
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name="Салон")
    photo = models.ImageField(upload_to="MastersPhoto/", verbose_name="Фотография")
    name = models.CharField(max_length=20, verbose_name="Имя")
    short_description = models.TextField(
        blank=True,
        verbose_name="Краткое описание",
        help_text="Текст отоброжаемый на странице со всеми мастерами",
    )
    description = CKEditor5Field("Описание", config_name="extends")
    works = models.ManyToManyField(Works, blank=True, verbose_name="Работы мастера")
    experience = models.PositiveIntegerField(default=0, verbose_name="Стаж работы")
    tattoo_type = models.ManyToManyField(
        TattooType, blank=True, verbose_name="Типы тату"
    )
    min_price = models.PositiveIntegerField(verbose_name="Минимальная цена")
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
        return f"Сеанс {self.day_of_week} {self.start_time} - {self.end_time}"


class SocialAccount(models.Model):
    master = models.ForeignKey(
        Master,
        verbose_name="Мастер",
        on_delete=models.CASCADE,
        related_name="social_account",
    )
    name = models.CharField(
        max_length=20,
        verbose_name="Название",
        help_text="Текст который будет отображен вместо ссылки",
    )
    icon = models.OneToOneField(
        SocialAccountIcon, on_delete=models.CASCADE, verbose_name="Иконка"
    )
    link = models.URLField(verbose_name="Ссылка")

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return self.link


class Consultation(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    types = models.ManyToManyField(
        TattooType,
        blank=True,
        verbose_name="Интересующие типы тату",
    )
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=100)
    status = models.BooleanField(
        default=False, verbose_name="Ответил", help_text="Мастер дал ответ клиенту"
    )

    class Meta:
        verbose_name = "Консультация"
        verbose_name_plural = "Консультация"

    def __str__(self):
        return self.client_email


class MasterReview(models.Model):
    RATING = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=100)
    status = models.BooleanField(
        default=False, verbose_name="Ответил", help_text="Мастер дал ответ клиенту"
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.user.username
