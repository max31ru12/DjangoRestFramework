from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField("name", max_length=64)
    last_name = models.CharField("lastname", max_length=64)
    email = models.CharField(
        max_length=64,
        unique=True
        
    )
    user_name = models.CharField("username", max_length=64)


# По поводу стандартной админки не совсем понял как ее делать, через стартаап админ
# или создать в модели класс админа?
