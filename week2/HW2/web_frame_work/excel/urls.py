import imp
from django.urls import path
from . import views
urlpatterns = [
    path('', views.simple_upload, name='upload'),
    path('about/', views.About, name='about'),
    path('search/', views.search_form, name='search-form'),
    path('studentlist/', views.list_student, name='student-list'),
    path('studentdietail/<int:id>/',views.detail_student,name='student-detail')
    
]
