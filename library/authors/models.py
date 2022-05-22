from django.db import models


class Author(models.Model):
    first_name = models.CharField("Имя", max_length=64)
    last_name = models.CharField("Фамилия", max_length=64)
    birthday_year = models.PositiveIntegerField()
