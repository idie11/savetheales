# Generated by Django 3.2.3 on 2021-06-14 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость товара')),
                ('is_instock', models.BooleanField(default=False, verbose_name='Наличие товара')),
                ('categories', models.ManyToManyField(related_name='products', to='products.Category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_image', verbose_name='Фото товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
            options={
                'verbose_name': 'Фото товара',
                'verbose_name_plural': 'Фото товаров',
            },
        ),
    ]