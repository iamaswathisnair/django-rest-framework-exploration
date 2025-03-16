
# from django.conf import settings
# from django.conf.urls.static import static

from django.urls import path
from .views import RestaurantListCreateAPI, RestaurantDetailAPI
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('restaurants/', RestaurantListCreateAPI.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantDetailAPI.as_view(), name='restaurant-detail'),
    path('token/', obtain_auth_token, name='get_token'),  # Login API
    
]


