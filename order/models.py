from django.db import models
from django.db.models import F, Sum


class Order(models.Model):
    CHOICES = (
        ('N','New'),
        ('W','Waiting'),
        ('O','On the way'),
        ('M','Order_is_made'),
        ('R','Rejected')
    )

    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=60)
    phone_number = models.CharField('Номер телефона', max_length=30)
    order_date = models.DateTimeField('Дата заказа', auto_now_add=True)
    address = models.CharField('Адресс', max_length=255)
    status = models.CharField('Статус', max_length=255, choices = CHOICES, default='N')
    total_price = models.DecimalField('Общая сумма', max_digits=10, decimal_places=2, null=True, blank=True, default=0)


    def get_total_price(self):
        return self.product_order.all().aggregate(total_price=Sum(F('quantity') * F('product__price')))['total_price']
        
        
    def save(self, *args, **kwargs):
        self.total_price = self.get_total_price()
        super(Order, self).save()