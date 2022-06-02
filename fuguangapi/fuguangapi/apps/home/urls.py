from django.urls import path, re_path
from . import views

urlpatterns = [
    path("test", views.HomeAPIView.as_view()),
]