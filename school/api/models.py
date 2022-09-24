from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    tre = [
        (1, 'Присужден'),
        (2, 'Не присужден')
    ]
    iin = models.IntegerField(default=0)
    patronymic = models.CharField(max_length=40)
    phone_number = models.IntegerField(default=0)
    status = models.CharField(choices=tre, default=2, max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username


class Document(models.Model):
    user = models.OneToOneField(User, models.CASCADE, default='')
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='document')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class CheckDocument(models.Model):
    Star = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]

    user = models.ForeignKey(User, models.CASCADE)
    document = models.ForeignKey(Document, models.CASCADE, verbose_name='просмотреть документ')
    star = models.IntegerField(choices=Star, default=1)











