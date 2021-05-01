from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    PRODUCTS_CHOISES = [('1', 'NEW'), ('2', 'REFURBISHED'), ('3', 'USED')]
    category = models.CharField(max_length=1, choices=PRODUCTS_CHOISES, default='1')
    description = models.CharField(max_length=600, blank=True, null=True)
    picture = models.ImageField(null=True, blank=True, upload_to='#', verbose_name='pic')
