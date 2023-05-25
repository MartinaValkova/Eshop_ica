from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#Database for products done by Martina
class Product(models.Model):
    
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

#Database for Order done by Martina

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    total = models.CharField(max_length=200)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'