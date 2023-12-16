from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Price']
admin.site.register(Product,ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'FirstName', 'LastName']
admin.site.register(Customer, CustomerAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'Rating', 'Review']
admin.site.register(Review, ReviewAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'Quantity', 'CreatedAt']
admin.site.register(Order, OrderAdmin)