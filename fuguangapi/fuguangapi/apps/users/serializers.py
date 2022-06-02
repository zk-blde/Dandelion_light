import re
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from fuguangapi.utils.authenticate import generate_jwt_token
from .models import User
from fuguangapi.settings import constants
class UserRegisterModelSerializer(serializers.ModelSerializer):
    """用户注册的序列化器"""
    re_password = serializers.CharField(max_length=16, required=True, write_only=True)
    code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True)
    token = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ["mobile", "password", "re_password", "code", "token"]
        extra_kwargs = {
            "mobile": {
                "write_only": True,
                "required": True,
                "min_length": 11,
            },
            "password":{
                "write_only": True,
                "required": True,
                "min_length": 6,
                "max_length": 16,
            }
        }
    def validate(self, data):
        """验证客户端数据"""
        # 手机号格式验证
        mobile = data.get("mobile",None)
        if not re.match("1[3-9]\d{9}", mobile):
            raise serializers.ValidationError(detail="手机号格式不正确！")
        # 密码和确认密码
        password = data.get("password")
        re_password = data.get("re_password")
        if password != re_password:
            raise serializers.ValidationError(detail="密码和确认密码不一致！")
        # 手机号是否已注册
        try:
            User.objects.get(mobile=mobile)
            raise serializers.ValidationError(detail="手机号已注册！")
        except User.DoesNotExist:
            pass
        # todo 验证短信验证码
        return data
    def create(self, validated_data):
        """保存用户信息，完成注册"""
        mobile = validated_data.get("mobile")
        user = User.objects.create_user(
            username=mobile,
            mobile=mobile,
            avatar=constants.DEFAULT_USER_AVATAR,
        )
        password = validated_data.get("password")

        user.token = generate_jwt_token(user)
        return user