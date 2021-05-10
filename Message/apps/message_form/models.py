from django.db import models

# Create your models here.
class Message(models.Model):# 继承models.Model
    # 定义字段
    # max_length为必填字段，对应数据库中的varchar类型，verbose_name可理解为注释，并设置为主键
    name = models.CharField(max_length=20, verbose_name="姓名",primary_key=True)
    # EmailField是在CharField上的封装，会检测是否为邮箱，按住CTRL+左键点入可看到，已经默认设置了max_length,为254
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=100, verbose_name="联系地址")
    # TextField不限字段长度
    message = models.TextField(verbose_name="留言信息")

    # 表中的meta信息
    class Meta:
        verbose_name = "留言信息"
        verbose_name_plural = verbose_name
        # 可以自己指定表名
        # 可以自己指定表名
        db_table = "message"

        # 若不指定表名，会生成名为message_form_message的表，表的命名为“app名称_类的名称(将大写转化为了小写)”