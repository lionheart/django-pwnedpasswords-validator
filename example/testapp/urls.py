from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path('accounts/register', views.account_register),
    path('accounts/', include('django.contrib.auth.urls')),
]
