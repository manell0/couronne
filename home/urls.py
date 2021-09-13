from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('reg_match/', views.reg_match, name='reg_match'),
    path('edit/', views.edit, name='edit'),
    path('update/', views.update, name='update'),
    path('couronne_info/',views.couronne_info, name="couronne_info"),
    path('register/',views.register, name="register"),
    path('user_login/',views.user_login, name="user_login"),
]