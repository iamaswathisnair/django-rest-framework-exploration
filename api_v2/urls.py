
# from django.conf import settings
# from django.conf.urls.static import static

from django.urls import path
from . import views
                 

urlpatterns = [
    path('teachers/teacher_list', views.teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', views.get_teacher_by_id, name='teacher-detail'),
    path('teachers/<int:pk>/update/', views.update_teacher, name='teacher-update'),
    path('teachers/<int:pk>/delete/', views.delete_teacher, name='teacher-delete'),
]