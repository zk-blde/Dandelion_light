from rest_framework.generics import ListAPIView
from .models import Nav
from fuguangapi.settings import constants
from .serializers import NavModelSerializer
class NavHeaderAPIView(ListAPIView):
    """头部导航"""
    queryset = Nav.objects.filter(is_show=True,is_delete=False,position=0).order_by("orders","-id").all()[:constants.NAV_HEADER_LENGTH]
    serializer_class = NavModelSerializer
class NavFooterAPIView(ListAPIView):
    """脚部导航"""
    queryset = Nav.objects.filter(is_show=True,is_delete=False,position=1).order_by("orders","-id").all()[:constants.NAV_FOOTER_LENGTH]
    serializer_class = NavModelSerializer