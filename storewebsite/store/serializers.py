from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = CustomUser
       fields = ['username', 'email', 'password']
       extra_kwargs = {'password': {'write_only': True}}


   def create(self, validated_data):
       user = CustomUser(
           username=validated_data['username'],
           email=validated_data['email']
       )
       user.set_password(validated_data['password'])
       user.save()
       return user
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
