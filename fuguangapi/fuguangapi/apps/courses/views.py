from rest_framework.generics import ListAPIView
from .models import CourseDiretion,CourseCategory,Course
from .serializers import CourseDiretionModelSerializer,CourseCategoryModelSerliazer,CourseModelSerializer
from rest_framework.filters import OrderingFilter
from .paginations import CourseListPageNumberPagination
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


class CourseListAPIView(ListAPIView):
    """课程列表接口"""
    serializer_class = CourseModelSerializer
    filter_backends = [OrderingFilter,]
    ordering_fields = ('id', 'students', 'orders')
    pagination_class = CourseListPageNumberPagination
    def get_queryset(self):
        """列表页数据"""
        diretion = int(self.kwargs.get("diretion", 0))
        category = int(self.kwargs.get("category", 0))
        queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders","id")
        # 只有在学习方向大于0的情况下才进行过滤
        if diretion > 0:
            queryset = queryset.filter(diretion=diretion)
        if category > 0:
            queryset = queryset.filter(category=category)
        return queryset.all()