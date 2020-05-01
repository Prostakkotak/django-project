from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<method>', views.delivery_method, name='delivery_method'),
    path('news/', views.news, name='news'),
    path('news_single/<pk>/', views.news_single, name='news_single'),
    path('news_single_delete/<pk>/', views.news_single_delete, name='news_single_delete'),
    path('offer_news/', views.offer_news, name='offer_news'),
    path('delete_news_comment/<pk>/', views.delete_news_comment, name='delete_news_comment'),
    path('vehisles/', views.vehisles, name='vehisles'),
    path('vehisles/<pk>/', views.vehisle_single, name='vehisle_single'),
    path('control/create_vehisle/', views.create_vehisle, name='create_vehisle'),
    path('control/delete_vehisle/<pk>/', views.delete_vehisle, name='delete_vehisle'),
    path('control/change_vehisle/<pk>/', views.change_vehisle, name='change_vehisle'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', views.registration, name='registration'),
    path('control/', views.control, name='control'),
    path('control/create_news/', views.create_news, name='create_news'),
    path('control/change_news/<pk>', views.change_news, name='change_news'),
    path('control/create_delivery_class/', views.create_delivery_class, name='create_delivery_class'),
    path('control/delete_delivery_class/<pk>/', views.delete_delivery_class, name='delete_delivery_class'),
    path('control/change_delivery_class/<pk>/', views.change_delivery_class, name='change_delivery_class'),
    path('control/proposed_news_demo/<pk>/', views.proposed_news_demo, name='proposed_news_demo'),
    path('control/delete_proposed_news/<pk>/', views.delete_proposed_news, name='delete_proposed_news'),
    path('control/confirmed_proposed_news/<pk>/', views.confirmed_proposed_news, name='confirmed_proposed_news'),
    path('control/show_quick_quote/<pk>/', views.show_quick_quote, name='show_quick_quote'),
    path('control/delete_quick_quote/<pk>/', views.delete_quick_quote, name='delete_quick_quote'),
]