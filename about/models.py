from django.db import models


class Events(models.Model):
    name_of_event = models.CharField('Название мероприятия', max_length=255)
    text = models.TextField('Основная информация про ивент')
    date_of_event = models.DateTimeField('Дата мероприятия')


class Contact(models.Model):
    email = models.EmailField('Email')
    phone = models.CharField('Номер телефона', max_length=30)
    address = models.CharField('Адрес', max_length=255)
    instagram = models.CharField('Instagram', max_length=255, blank=True, null=True)
    whatsapp = models.CharField('''What's App''', max_length=255, blank=True, null=True)



