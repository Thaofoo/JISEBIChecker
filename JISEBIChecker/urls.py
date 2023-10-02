from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('logged/', views.indexLogged),
    path('manuscripts/', include('apps.manuscripts.urls')),
    path('accounts/', include('apps.accounts.urls')),
    
]
