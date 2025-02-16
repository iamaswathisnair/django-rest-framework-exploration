
# from django.conf import settings
# from django.conf.urls.static import static

from django.urls import path
from .views import RestaurantListCreateAPI, RestaurantDetailAPI

urlpatterns = [
    path('restaurants/', RestaurantListCreateAPI.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantDetailAPI.as_view(), name='restaurant-detail'),
]
