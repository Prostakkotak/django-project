from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<method>', views.delivery_method, name='delivery_method'),
    path('news/', views.news, name='news'),
    path('news_single/<pk>/', views.news_single, name='news_single'),
    path('vehisles/', views.vehisles, name='vehisles'),
    path('accounts/', include('django.contrib.auth.urls')),
]