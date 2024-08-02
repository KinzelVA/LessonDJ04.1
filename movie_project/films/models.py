# films/models.py
from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100)  # Поле для названия фильма
    description = models.TextField()  # Поле для описания фильма
    review = models.TextField()  # Поле для отзыва

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
