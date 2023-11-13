from django.db import models


class Coordinates(models.Model):
    cadastral_numb = models.PositiveIntegerField(
        "Кадастровый номер",
        blank=False,
    )
    latitude = models.FloatField(
        "Широта",
        blank=False,
        help_text='Введите широту'
    )
    longitude = models.FloatField(
        "Долгота",
        blank=False,
        help_text='Введите долготу'
    )


class Result(models.Model):
    coordinates = models.OneToOneField(
        Coordinates,
        on_delete=models.CASCADE,
        blank=False,
        null=True,
        verbose_name="Координаты"
    )
    t_or_f = models.BooleanField(
        verbose_name="Правда или нет"
    )
