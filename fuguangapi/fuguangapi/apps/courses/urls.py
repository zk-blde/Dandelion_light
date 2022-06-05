from django.urls import path,re_path
from . import views

urlpatterns = [
    path("diretion", views.CourseDiretionListAPIView.as_view()),
    re_path("^category/(?P<diretion>\d+)$", views.CourseCategoryListAPIView.as_view()),
    re_path("^(?P<diretion>\d+)/(?P<category>\d+)$", views.CourseListAPIView.as_view()),
]