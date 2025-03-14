
# from django.conf import settings
# from django.conf.urls.static import static

from django.urls import path,include
from . import views 
                 

urlpatterns = [
    path('books/', views.BookAPIView.as_view(), name='book-list'),  # ✅ Correct for CBV
    path('books/<int:pk>/', views.BookDetailAPIView.as_view(), name='book-detail'),  # ✅ Correct for CBV
     path('api-auth/', include('rest_framework.urls')),  # This enables login/logout UI

]
#   path('books/', BookAPIView.as_view(), name='book-list'),