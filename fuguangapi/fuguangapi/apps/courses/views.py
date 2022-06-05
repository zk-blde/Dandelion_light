from rest_framework.generics import ListAPIView
from .models import CourseDiretion
from .serializers import CourseDiretionModelSerializer
# Create your views here.
class CourseDiretionListAPIView(ListAPIView):
    queryset = CourseDiretion.objects.filter(is_show=True, is_delete=False).order_by("orders","id")
    serializer_class = CourseDiretionModelSerializer
    pagination_class = None