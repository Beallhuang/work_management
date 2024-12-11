from django.db import models


class OutputLogs(models.Model):
    """操作日志表"""

    id = models.AutoField(primary_key=True)
    re_time = models.CharField(max_length=32, verbose_name='请求时间')
    re_user = models.CharField(max_length=32, verbose_name='操作人')
    re_ip = models.CharField(max_length=32, verbose_name='请求IP')
    re_url = models.CharField(max_length=255, verbose_name='请求url')
    re_method = models.CharField(max_length=11, verbose_name='请求方法')
    re_content = models.TextField(null=True, verbose_name='请求参数')
    rp_content = models.TextField(null=True, verbose_name='响应参数')
    access_time = models.IntegerField(verbose_name='响应耗时/ms')

    class Meta:
        db_table = 'op_logs'
        verbose_name = '访问日志'
        verbose_name_plural = verbose_name

class AccessTimeOutLogs(models.Model):
    """超时操作日志表"""

    id = models.AutoField(primary_key=True)
    re_time = models.CharField(max_length=32, verbose_name='请求时间')
    re_user = models.CharField(max_length=32, verbose_name='操作人')
    re_ip = models.CharField(max_length=32, verbose_name='请求IP')
    re_url = models.CharField(max_length=255, verbose_name='请求url')
    re_method = models.CharField(max_length=11, verbose_name='请求方法')
    re_content = models.TextField(null=True, verbose_name='请求参数')
    rp_content = models.TextField(null=True, verbose_name='响应参数')
    access_time = models.IntegerField(verbose_name='响应耗时/ms')

    class Meta:
        db_table = 'access_timeout_logs'
        verbose_name = '访问超时日志'
        verbose_name_plural = verbose_name


from django.contrib.admin.models import CHANGE, DELETION, ADDITION, LogEntry

class AdminUserLog(LogEntry):
    class Meta:
        proxy = True
        verbose_name = '表行级操作日志'
        verbose_name_plural = '表行级操作日志'