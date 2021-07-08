from django.db import models
from django.utils.timezone import datetime
from django.utils import timezone as tz





class Reserve(models.Model):
    user = models.ForeignKey("users.User", verbose_name=("user_reserve"), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('Имя', max_length=255)
    reserve_datetime = models.DateTimeField('Дата и время')
    people_quantity = models.PositiveIntegerField('Количество людей')
    phone_number = models.PositiveIntegerField('Номер телефона')


    def __str__(self):
        return self.name


    # def check_date(self):
    #     if tz.now() < self.reserve_datetime:
    #         return 'Bar closed'
        
    
    def save(self, *args, **kwargs):
        # self.reserve_datetime = self.check_date()
        return super(Reserve, self).save()
    