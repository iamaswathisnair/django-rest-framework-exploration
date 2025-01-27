
# from django.conf import settings
# from django.conf.urls.static import static

from django.urls import path
from . import views
                 

urlpatterns = [
    path('student-details/', views.student_details, name='student-details'),
    path('all_student/', views.all_student, name='all_student'),
    
  
    path('students/', views.student_list, name='student_list'),  # GET all students
    path('students/<int:pk>/', views.student_detail, name='student_detail'),  # GET single student
    path('students/create/', views.student_create, name='student_create'),  # POST new student
    path('students/update/<int:pk>/', views.student_update, name='student_update'),  # PUT full update
    path('students/partial-update/<int:pk>/', views.student_partial_update, name='student_partial_update'),  # PATCH partial update
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),  # DELETE student
    
]