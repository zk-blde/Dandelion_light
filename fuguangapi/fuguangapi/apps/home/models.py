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
