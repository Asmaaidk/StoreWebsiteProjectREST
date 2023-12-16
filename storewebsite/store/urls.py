from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pruducts', ProductsViewSet, basename='pruducts')
router.register('customers', CustomersViewSet, basename='customers')
router.register('reviews', ReviewsViewSet, basename='reviews')
router.register('orders', OrdersViewSet, basename='orders')


urlpatterns = [
  path('viewset/', include(router.urls)),
  path('viewset/<int:pk>/', include(router.urls)),
]


