from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    address = models.CharField('Адрес', max_length=255)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=255)
    dob = models.DateField('Дата рождения', null=True)
    # email = models.EmailField(db_index=True, unique=True)
    is_staff = models.BooleanField(default=False)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
    
    # def _generate_jwt_token(self):
    #     """
    #     Генерирует веб-токен JSON, в котором хранится идентификатор этого
    #     пользователя, срок действия токена составляет 1 день от создания
    #     """
    #     dt = datetime.now() + timedelta(days=1)

    #     token = jwt.encode({
    #         'id': self.pk,
    #         'exp': int(dt.strftime('%s'))
    #     }, settings.SECRET_KEY, algorithm='HS256')

    #     return token.decode('utf-8')


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Review(models.Model):
    phone_number = models.IntegerField('Номер телефона')
    text = models.TextField('Отзыв')