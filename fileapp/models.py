from django.db import models
from django.contrib.auth.models import User

class Directory(models.Model):
    name = models.CharField(max_length=255,  verbose_name='文件夹')
    path = models.TextField(verbose_name='路径')
    users = models.ManyToManyField(User, related_name='directories', verbose_name='用户')  # Many-to-many relation to user

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '目录'
        verbose_name_plural = '目录'


class FileManage(models.Model):
    pass

    class Meta:
        verbose_name = '文件管理'
        verbose_name_plural = '文件管理'