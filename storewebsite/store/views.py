from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# authentication_classes = [SessionAuthentication, BasicAuthentication]
authentication_classes = [TokenAuthentication]
permission_classes = [IsAuthenticated]

class ProductsViewSet(viewsets.ModelViewSet):
   serializer_class = ProductsSerializer
   queryset = Product.objects.all()

class CustomersViewSet(viewsets.ModelViewSet):
   serializer_class = CustomersSerializer
   queryset = Customer.objects.all()

class ReviewsViewSet(viewsets.ModelViewSet):
   serializer_class = ReviewsSerializer
   queryset = Review.objects.all()

class OrdersViewSet(viewsets.ModelViewSet):
   serializer_class = OrdersSerializer
   queryset = Order.objects.all()