from django.urls import path
from crud import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
]
