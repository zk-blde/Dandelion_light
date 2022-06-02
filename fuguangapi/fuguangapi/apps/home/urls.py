from django.urls import path,re_path
from . import views
urlpatterns = [
    path("nav/header", views.NavHeaderAPIView.as_view()),
    path("nav/footer", views.NavFooterAPIView.as_view()),
    path("banner", views.BannerAPIView.as_view()),
]