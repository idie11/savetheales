from django.db import models


class Category(models.Model):
    name = models.CharField('Название категории', max_length=255)
    

   
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название товара', max_length=255)
    description = models.TextField('Описание товара')
    price = models.DecimalField('Стоимость товара', max_digits=10, decimal_places=2)
    is_instock = models.BooleanField('Наличие товара', default=False)
    categories = models.ManyToManyField(Category, related_name='products')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name    


class ProductImage(models.Model):
    product = models.ForeignKey('products.Product', models.CASCADE, 'images')
    image = models.ImageField('Фото товара', upload_to='product_image')


    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'

    def __str__(self):
        return self.product.name