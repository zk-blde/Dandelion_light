from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True, verbose_name='手机号')
    money  = models.DecimalField(max_digits=9, default=0.0, decimal_places=2, verbose_name="钱包余额")
    credit = models.IntegerField(default=0, verbose_name="积分" )
    avatar = models.ImageField(upload_to="avatar/%Y/", null=True, default="", verbose_name="个人头像")
    class Meta:
        db_table = 'fg_users'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
