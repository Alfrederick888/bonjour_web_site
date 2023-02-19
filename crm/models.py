from django.db import models

class Order(models.Model):
    data = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=200, verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

