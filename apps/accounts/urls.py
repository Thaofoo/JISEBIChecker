from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name="login"),
    path("register/", views.register, name="full-report")
]