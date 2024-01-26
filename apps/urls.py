from django.contrib import admin
from django.urls import path

from apps.views import IndexView, RegisterView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register-pages/', RegisterView, name='register')
]
