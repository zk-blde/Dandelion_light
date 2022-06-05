from rest_framework.generics import ListAPIView
from .models import CourseDiretion,CourseCategory
from .serializers import CourseDiretionModelSerializer,CourseCategoryModelSerliazer
# Create your views here.
class CourseDiretionListAPIView(ListAPIView):
    """学习方向列表"""
    queryset = CourseDiretion.objects.filter(is_show=True, is_delete=False).order_by("orders","id")
    serializer_class = CourseDiretionModelSerializer
    pagination_class = None
class CourseCategoryListAPIView(ListAPIView):
    """课程分类列表"""
    queryset = CourseCategory.objects.filter(is_show=True, is_delete=False).order_by("orders","id")
    serializer_class = CourseCategoryModelSerliazer
    pagination_class = None