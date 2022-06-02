from rest_framework_jwt.views import ObtainJSONWebToken
from .models import User
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
class LoginAPIView(ObtainJSONWebToken):
    """用户登录视图"""
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterModelSerializer
class UserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterModelSerializer

from rest_framework.views import APIView
from .models import User
class MobileAPIView(APIView):
    def get(self,request,mobile):
        """校验手机号是否已注册"""
        try:
            User.objects.get(mobile=mobile)
            return Response({"errmsg":"当前手机号已注册！"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            # 如果查不到该手机号的注册记录，则证明手机号可以注册使用
            return Response({"errmsg":"OK"}, status=status.HTTP_200_OK)
