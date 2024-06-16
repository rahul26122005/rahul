from django.contrib import admin
from django.urls import path
from university import views
from .views import home, register


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('group_specific/', views.group_specific_view, name='group_specific'),
    path('upload_students/', views.upload_student_file, name='upload_students'),
    path('select_class/', views.select_class, name='select_class'),
    path('Attendance/', views.view1, name='take_attendance'),
    path('generate_report/', views.view2, name='generate_report'),
    path('success/', views.success, name='success'),
    path('download_template/', views.download_template, name='download_template'),
    path('generate_individual_reports/', views.generate_individual_reports, name='generate_individual_reports'),
]


