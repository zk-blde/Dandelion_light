from rest_framework_jwt.utils import jwt_payload_handler as payload_handler

def jwt_payload_handler(user):
    """
    自定义载荷信息
    @params user: 用户模型实例对象
    """
    # 先让jwt模块生成自己的载荷信息
    payload = payload_handler(user)
    # 追加自己要返回的内容
    if hasattr(user, 'avatar'):
        payload['avatar'] = user.avatar.url if user.avatar else ""
    if hasattr(user, 'nickname'):
        payload['nickname'] = user.nickname

    if hasattr(user, 'money'):
        payload['money'] = float(user.money)
    if hasattr(user, 'credit'):
        payload['credit'] = user.credit

    return payload

import re
from django.contrib.auth.backends import BaseBackend,UserModel
def get_user_by_account(account):
    """
    根据帐号信息获取user模型实例对象
    :param account: 账号信息，可以是用户名，也可以是手机号，甚至其他的可用于识别用户身份的字段信息
    :return: User对象 或者 None
    """
    try:
        if re.match('^1[3-9]\d{9}$', account):
            # 帐号为手机号
            user = UserModel.objects.get(mobile=account)
        else:
            # 帐号为用户名
            user = UserModel.objects.get(username=account)
    except UserModel.DoesNotExist:
        return None
    else:
        return user

from django.contrib.auth.backends import ModelBackend,UserModel
class CustomAuthBackend(ModelBackend):
    """
    自定义用户认证类
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        if user is not None and user.check_password(password) and self.user_can_authenticate(user):
            return user


from rest_framework_jwt.settings import api_settings
def generate_jwt_token(user):
    """
    生成jwt token
    @params user: 用户模型实例对象
    """
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)