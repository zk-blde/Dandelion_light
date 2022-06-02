from rest_framework.generics import ListAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
class CacheListAPIView(ListAPIView):
    @method_decorator(cache_page(60 * 60 * 24))
    def get(self, request, *args, **kwargs):
        # print("获取列表页信息....")
        return self.list(request, *args, **kwargs)