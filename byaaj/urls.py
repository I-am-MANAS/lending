from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutt, name='logout'),
    path('home/', views.home, name='home'),
    path('', views.random, name='random'),
    path('user/', views.userpage, name='user'),
    path('customer/', views.customer, name='customer'),
    path('interest/', views.interest, name='interest'),
]
