from django.db import models

class Categorys(models.Model):
    name = models.CharField( max_length=250)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    author = models.CharField( max_length=250)
    price = models.FloatField()
    name = models.CharField( max_length=250)
    stock = models.IntegerField()
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.URLField( max_length=400)
    date_created = models.DateField( auto_now_add=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_tag = models.CharField(max_length=16)
    price = models.FloatField()
    name = models.CharField( max_length=250)
    stock = models.IntegerField()
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    image = models.URLField( max_length=400)
    date_created = models.DateField( auto_now_add=True)
    state = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    