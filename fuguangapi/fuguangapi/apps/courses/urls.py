from django.urls import path,re_path
from . import views
urlpatterns = [
    path("diretion", views.CourseDiretionListAPIView.as_view())
]