from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.Signup, name="signup"),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name="about"),
    path('login/', views.loginn, name="login"),
    path('order/', views.order, name="order"),
    path('menu/', views.menu, name="menu"),
    path('logout/', views.logouts, name="logout"),
    path('search/', views.search, name="search"),
    path('read', views.read, name="read"),
    path('review/', views.review, name="review"),
    path('payment', views.payment, name="payment"),
    path('bill/', views.bill, name="bill")
]