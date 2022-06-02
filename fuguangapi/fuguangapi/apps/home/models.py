from fuguangapi.utils.models import BaseModel, models
class Nav(BaseModel):
    # django默认创建ID
    POSITION_CHOICES = (
        # (值, "描述信息"),
        # 模型对象.get_字段名_display()  ==> 描述信息
        # 模型对象.字段名    ===> 值
        (0, "头部"),
        (1, "脚部"),
    )
    class Meta:
        db_table = "fg_nav"
        verbose_name = "导航信息"
        verbose_name_plural = verbose_name
    link = models.CharField(max_length=500, verbose_name="链接地址")
    is_http = models.BooleanField(default=False, verbose_name="是否外链")
    position = models.SmallIntegerField(default=0, choices=POSITION_CHOICES, verbose_name="导航位置")


class Banner(BaseModel):
    class Meta:
        db_table = "fg_banner"
        verbose_name = "轮播广告"
        verbose_name_plural = verbose_name
    # 图片保存默认是在当前服务器，真实存放地址会使用配置中的MADIE_ROOT+upload_to
    image = models.ImageField(upload_to="banner/%Y/", verbose_name="图片地址")
    note = models.CharField(max_length=150, verbose_name='备注信息')
    link = models.CharField(max_length=500, verbose_name="链接地址")
    is_http = models.BooleanField(default=False, verbose_name="是否外链")