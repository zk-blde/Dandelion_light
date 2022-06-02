from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_redis import get_redis_connection
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
class HomeAPIView(APIView):
    # django提供的视图缓存，保存的位置就是default设置的redis0号库
    @method_decorator(cache_page(5))
    def get(self,request):
        """测试"""
        print("hello")
        # 直接操作redis
        redis = get_redis_connection("default")
        brother = redis.lrange("brother",0,-1)
        # django提供的缓存api操作
        from django.core.cache import caches
        sms_redis = caches["sms_code"]
        sms_redis.set("sms_1331234546","12323",30)
        return Response(brother, status.HTTP_200_OK)