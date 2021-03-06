# Generated by Django 3.2.3 on 2021-06-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=60, verbose_name='Фамилия')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('address', models.CharField(max_length=255, verbose_name='Адресс')),
                ('status', models.CharField(choices=[('N', 'New'), ('W', 'Waiting'), ('O', 'On the way'), ('M', 'Order_is_made'), ('R', 'Rejected')], default='N', max_length=255, verbose_name='Статус')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Общая сумма')),
            ],
        ),
    ]
