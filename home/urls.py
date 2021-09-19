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
    path('profile/',views.profile, name="profile"),
    path('league_all/',views.league_all, name="league_all"),
    path('contact_us/',views.contact_us, name="contact_us"),
    path('succes_contact_us/',views.succes_contact_us, name="succes_contact_us"),
]