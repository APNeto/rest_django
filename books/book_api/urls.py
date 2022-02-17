from django.contrib import admin
from django.urls import path
from book_api.views import book_list

urlpatterns = [
    path('', book_list)
]