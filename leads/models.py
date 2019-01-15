from django.db import models


class Leads(models.Model):
    name = models.CharField(max_length=100,verbose_name="lead名字", help_text="lead名字")
    email = models.EmailField(verbose_name="邮箱", help_text="邮箱")
    message = models.CharField(max_length=300, verbose_name="信息", help_text="信息")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间", help_text="创建时间")
