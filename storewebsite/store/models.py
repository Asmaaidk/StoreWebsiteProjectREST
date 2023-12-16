from django.db import models


# Create your models here.

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=8, decimal_places=2)

class Customer(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)

class Review(models.Model):
    Rating = models.FloatField()
    Review = models.TextField()
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Order(models.Model):
    Quantity = models.IntegerField()
    CreatedAt = models.DateTimeField()
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
