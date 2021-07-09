from django.db import models
from django.db.models import F, Sum



# class Order(models.Model):
#     product = models.ManyToManyField('products.Product', related_name='orders')
#     date = models.DateTimeField(default=timezone.now)
#     quantity = models.ManyToManyField('products.Product', through='quantity', related_name='orders_quantity')
#     total_price = models.DecimalField('Общая сумма', max_digits=10, decimal_places=2, null=True, blank=True, default=0)

#     def get_total_price(self):
#         return self.product_order.all().aggregate(total_price=Sum(F('quantity') * F('product__price')))['total_price']
        

#     def __str__(self):
#         return '{}+{}'.format(self.product,  self.quantity)

class Order(models.Model):
    # CHOICES = (
    #     ('N','New'),
    #     ('W','Waiting'),
    #     ('O','On the way'),
    #     ('M','Order_is_made'),
    #     ('R','Rejected')
    # )

    customer = models.ForeignKey('users.User', models.CASCADE, 'orders_cust', null=True, blank=True)
    order_date = models.DateTimeField('Дата заказа', auto_now_add=True)
    address = models.CharField('Адресс', max_length=255)
    # status = models.CharField('Статус', max_length=255, choices = CHOICES, default='N')
    total_price = models.DecimalField('Общая сумма', max_digits=10, decimal_places=2, null=True, blank=True, default=0)


    def get_total_price(self):
        return self.product_order.all().aggregate(total_price=Sum(F('quantity') * F('product__price')))['total_price']
        
        
    def save(self, *args, **kwargs):
        self.total_price = self.get_total_price()
        super(Order, self).save()

    def __str__(self):
        return self.address

class OrderProduct(models.Model):
    quantity = models.PositiveIntegerField('Количество', default=1)
    product = models.ForeignKey('products.Product', models.CASCADE, 'orders')
    order = models.ForeignKey(Order, models.CASCADE, 'product_order')





