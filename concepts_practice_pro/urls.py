
from django.contrib import admin
from django.urls import path , include
 

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')  ),
    path('api/v2/', include('api_v2.urls')  ),
    path('api/v3/',   include('api_cbvs.urls')  ),
    path('api/v4/' ,    include('api_generic.urls') ),
    path('api/v5/' ,      include('generic_prebuilt.urls') ),

  
]

