from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<method>', views.delivery_method, name='delivery_method'),
    path('news/', views.news, name='news'),
    path('news_single/<pk>/', views.news_single, name='news_single'),
    path('news_single_delete/<pk>', views.news_single_delete, name='news_single_delete'),
    path('delete_news_comment/<pk>/', views.delete_news_comment, name='delete_news_comment'),
    path('vehisles/', views.vehisles, name='vehisles'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', views.registration, name='registration'),
]