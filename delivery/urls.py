from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('news/', views.NewsPage.as_view(), name='news'),
    path('delivery_order/', views.DeliveryOrder.as_view(), name='delivery_order'),
    path('control/delete_delivery_order/<pk>/', views.DeleteDeliveryOrder.as_view(), name='delete_delivery_order'),
    path('control/show_delivery_order/<pk>/', views.ShowDeliveryOrder.as_view(), name='show_delivery_order'),
    path('news_single/<pk>/', views.NewsSingle.as_view(), name='news_single'),
    path('news_single_delete/<pk>/', views.DeleteSingleNews.as_view(), name='news_single_delete'),
    path('offer_news/', views.OfferNews.as_view(), name='offer_news'),
    path('delete_news_comment/<pk>/', views.DeleteNewsComment.as_view(), name='delete_news_comment'),
    path('vehisles/', views.VehislesPage.as_view(), name='vehisles'),
    path('vehisles/<pk>/', views.VehisleSingle.as_view(), name='vehisle_single'),
    path('control/create_vehisle/', views.CreateVehisle.as_view(), name='create_vehisle'),
    path('control/delete_vehisle/<pk>/', views.DeleteVehisle.as_view(), name='delete_vehisle'),
    path('control/change_vehisle/<pk>/', views.ChangeVehisle.as_view(), name='change_vehisle'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', views.Registration.as_view(), name='registration'),
    path('control/', views.Control.as_view(), name='control'),
    path('control/create_news/', views.CreateNews.as_view(), name='create_news'),
    path('control/change_news/<pk>', views.ChangeNews.as_view(), name='change_news'),
    path('control/create_delivery_class/', views.CreateDeliveryClass.as_view(), name='create_delivery_class'),
    path('control/delete_delivery_class/<pk>/', views.DeleteDeliveryClass.as_view(), name='delete_delivery_class'),
    path('control/change_delivery_class/<pk>/', views.ChangeDeliveryClass.as_view(), name='change_delivery_class'),
    path('control/proposed_news_demo/<pk>/', views.proposed_news_demo, name='proposed_news_demo'),
    path('control/delete_proposed_news/<pk>/', views.DeleteProposedNews.as_view(), name='delete_proposed_news'),
    path('control/confirmed_proposed_news/<pk>/', views.ConfirmedProposedNews.as_view(), name='confirmed_proposed_news'),
    path('control/show_quick_quote/<pk>/', views.ShowQuickQuote.as_view(), name='show_quick_quote'),
    path('control/delete_quick_quote/<pk>/', views.DeleteQuickQuote.as_view(), name='delete_quick_quote'),
]