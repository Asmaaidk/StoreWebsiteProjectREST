from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pruduct', ProductsViewSet, basename='pruduct')
router.register('customer', CustomersViewSet, basename='customer')
router.register('review', ReviewsViewSet, basename='review')
router.register('order', OrdersViewSet, basename='order')


urlpatterns = [
  path('viewset/', include(router.urls)),
  path('viewset/<int:pk>/', include(router.urls)),
]


