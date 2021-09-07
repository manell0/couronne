from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('reg_match/', views.reg_match, name='reg_match'),
    path('edit/', views.edit, name='edit'),
    path('update/', views.update, name='update'),
    path('upp/', views.upp, name='upp'),
    path('couronne_info/',views.couronne_info, name="couronne_info"),
    path('register/',views.register, name="register"),
]