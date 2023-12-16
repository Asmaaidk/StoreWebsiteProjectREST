from rest_framework import serializers
from .models import *

class ProductsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Product
       fields = ['id', 'Name', 'Price']

class CustomersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Customer
       fields = ['id', 'FirstName', 'LastName']

class ReviewsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Review
       fields = ['id', 'Rating', 'Review', 'ProductID', 'CustomerID']

class OrdersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Order
       fields = ['id', 'Quantity', 'CreatedAt', 'ProductID', 'CustomerID']
