from django.db import models, connections


class Movie(models.Model):
    title = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=5)
    ratings = models.CharField(max_length=3)
    metascore = models.CharField(max_length=5)
    votes = models.CharField(max_length=10)
    gross_income = models.CharField(max_length=10)

    class Meta:
        db_table = "movies"
        ordering = ['year']


class Weather(models.Model):
    night_period = models.CharField(max_length=15)
    day_period = models.CharField(max_length=15)
    night_temp = models.CharField(max_length=5)
    day_temp = models.CharField(max_length=5)
    night_humidity = models.CharField(max_length=5)
    day_humidity = models.CharField(max_length=5)

    class Meta:
        db_table = "weather"

class EcommerceLazada(models.Model):
    prod_name = models.CharField(max_length=120)
    price = models.CharField(max_length=10, default='0')

    class Meta:
        db_table = "lazada"

class EcommerceShopee(models.Model):
    prod_name = models.CharField(max_length=120)
    price = models.CharField(max_length=10, default='0')

    class Meta:
        db_table = "shopee"