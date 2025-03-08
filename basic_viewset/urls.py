from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

# Create a router and register the ViewSet
router = DefaultRouter()    #creates a router object, which will automatically generate REST API URLs.
router.register(r'movies', MovieViewSet, basename='movie')  # Register the ViewSet with the router

# Include the router URLs in urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # 🚀 This adds all ViewSet routes automatically /  Add the router URLs to urlpatterns
]
