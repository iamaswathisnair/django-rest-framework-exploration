
from django.urls import path, include
from rest_framework.routers import DefaultRouter  # A magic URL maker!
from .views import JobPostingViewSet  # Import our robot

router = DefaultRouter()
router.register(r'jobs', JobPostingViewSet)  # "Hey robot, handle all URLs starting with /jobs/"

urlpatterns = [
    path('', include(router.urls)),  
]