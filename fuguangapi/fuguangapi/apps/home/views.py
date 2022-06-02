from rest_framework.generics import ListAPIView
from .models import Nav, Banner
from fuguangapi.settings import constants
from .serializers import NavModelSerializer, BannerModelSerializer
from fuguangapi.utils.views import CacheListAPIView

class NavHeaderAPIView(CacheListAPIView):
    """头部导航"""
    queryset = Nav.objects.filter(is_show=True, is_delete=False, position=0).order_by("orders", "-id").all()[
               :constants.NAV_HEADER_LENGTH]
    serializer_class = NavModelSerializer


class NavFooterAPIView(CacheListAPIView):
    """脚部导航"""
    queryset = Nav.objects.filter(is_show=True, is_delete=False, position=1).order_by("orders", "-id").all()[
               :constants.NAV_FOOTER_LENGTH]
    serializer_class = NavModelSerializer


class BannerAPIView(CacheListAPIView):
    """轮播广告"""
    queryset = Banner.objects.filter(is_show=True, is_delete=False, ).order_by("orders", "-id").all()[
               :constants.BANNER_LENGTH]
    serializer_class = BannerModelSerializer
