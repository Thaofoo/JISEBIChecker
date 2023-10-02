from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload, name="upload"),
    path("full-report", views.full_report, name="full-report"),
    path("report", views.report, name="report")
]

