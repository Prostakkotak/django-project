from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<method>', views.delivery_method, name='delivery_method'),
    path('news/', views.news, name='news'),
    path('news_single/<pk>/', views.news_single, name='news_single'),
    path('news_single_delete/<pk>', views.news_single_delete, name='news_single_delete'),
    path('offer_news/', views.offer_news, name='offer_news'),
    path('delete_news_comment/<pk>/', views.delete_news_comment, name='delete_news_comment'),
    path('vehisles/', views.vehisles, name='vehisles'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', views.registration, name='registration'),
    path('control/', views.control, name='control'),
    path('control/create_news', views.create_news, name='create_news'),
    path('control/change_news/<pk>', views.change_news, name='change_news'),
    path('control/create_vehisle', views.create_vehisle, name='create_vehisle'),
    path('control/create_delivery_class', views.create_delivery_class, name='create_delivery_class'),
]