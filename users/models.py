from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    address = models.CharField('Адрес', max_length=255)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=255)
    dob = models.DateField('Дата рождения', null=True)
    

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'