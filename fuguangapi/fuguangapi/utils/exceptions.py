import logging
from django.db import DatabaseError
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
logger = logging.getLogger("django")
def custom_exception_handler(exc, context):
    """
    自定义异常处理函数
    :param exc: 本次发生的异常实例对象
    :param context: 抛出异常的上下文
    :return: Response响应对象
    """
    # 1. 先让drf内置的异常处理函数先解决它能识别的异常
    response = exception_handler(exc, context)
    if response is None:
        # 2. drf无法识别的异常
        view = context["view"]
        if isinstance(exc, DatabaseError):
            # 记录日志
            logger.error('数据库操作异常！[%s] %s' % (view, exc))
            response = Response({'errmsg': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        elif isinstance(exc, ZeroDivisionError):
            logger.error('计算异常！[%s] %s' % (view, exc))
            response = Response({'errmsg': '除数不能为0!'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return response