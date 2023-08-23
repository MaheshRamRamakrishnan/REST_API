from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('a/', views.drink_list),
    path('a/<int:id>/', views.drink_detail),

]
