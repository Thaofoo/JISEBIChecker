from django.urls import path
from . import views

urlpatterns = [
    path("full-report", views.full_report, name="full-report")
]