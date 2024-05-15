from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    longitude = models.CharField(max_length=100, verbose_name="Долгота")
    latitude = models.CharField(max_length=100, verbose_name="Широта")


class AboutBlock(models.Model):
    image = models.ImageField(upload_to="Site/AboutImages/",verbose_name="Картинка")
    title = models.CharField(max_length=50,
                             verbose_name="Заголовок")
    short_description = models.TextField(verbose_name="Краткое описание",
                                         help_text="Текст отоброжаемый на главной странице")
    description = models.TextField(verbose_name="Подробное описание",
                                   help_text="текст используемый на подробной странице")
    icon = models.ImageField(upload_to="Site/AboutIcons/",
                             verbose_name="Иконка",
                             help_text="Иконка на главной странице")

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self):
        return self.title