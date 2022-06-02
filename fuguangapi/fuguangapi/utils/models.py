from django.db import models
class BaseModel(models.Model):
    """公共模型"""
    name = models.CharField(max_length=100, verbose_name="名称/标题")
    orders = models.IntegerField(default=1, verbose_name="排序")
    is_show = models.BooleanField(default=True, verbose_name="是否显示")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    # auto_now_add 添加数据时，会把当前时间戳作为默认值保存到字段中
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    # auto_now 每次数据改动，都会把当前时间戳作为默认值保存到字段中
    updated_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")
    class Meta:
        # 设置当前模型类并非真正的模型，而是一种公共代码的抽象模型
        # 这种模型在数据迁移中不会被当做数据模型来创建数据表
        abstract = True
    def __str__(self):
        return f"<{self.__class__.__name__} {self.name}>"