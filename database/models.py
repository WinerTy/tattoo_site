from django.db import models


class Works(models.Model):
    photo = models.ImageField(upload_to="WorksPhoto/", verbose_name="Фотография")
    name = models.CharField(max_length=30, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

    def __str__(self):
        return self.name


class Master(models.Model):
    photo = models.ImageField(upload_to="MastersPhoto/", verbose_name="Фотография")
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


class Note(models.Model):
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.client_email
