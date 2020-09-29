from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='имя')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='имя')
    photo = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(max_length=500, verbose_name='краткое описание товара', blank=True)
    description = models.TextField(verbose_name='подробное описание товара')
    specifications = models.TextField(verbose_name='характеристики товара')
    price = models.DecimalField(verbose_name='цена товара', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name
