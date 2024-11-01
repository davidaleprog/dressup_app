from django.urls import path
from . import views

# URL configuration for dressup_app
# The `urlpatterns` list routes URLs to views.
# pattern : ' route ', view, name=' name '
urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('create/', views.item_create, name='item_create'),
    path('<int:pk>/edit/', views.item_update, name='item_update'),
    path('<int:pk>/delete/', views.item_delete, name='item_delete'),
    path('outfits/', views.outfit_list, name='outfit_list'),
    path('outfits/<int:pk>/', views.outfit_detail, name='outfit_detail'),
    path('outfits/create/', views.outfit_create, name='outfit_create'),
    path('outfits/<int:pk>/edit/', views.outfit_update, name='outfit_update'),
    path('outfits/<int:pk>/delete/', views.outfit_delete, name='outfit_delete'),
]

