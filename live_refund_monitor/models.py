from django.db import models

# Create your models here.
class ItemInfoLive(models.Model):
    brand_name = models.CharField(max_length=50, verbose_name='品牌')
    activity_name = models.CharField(max_length=50, verbose_name='活动名称')
    commodity_desc =  models.CharField(max_length=200, verbose_name='商品描述')
    commodity_style_no = models.CharField(max_length=50, verbose_name='系统款号')
    commodity_no = models.CharField(max_length=50, verbose_name='系统货号')
    item_id = models.CharField(max_length=20, verbose_name='外部商品ID')
    live_start_time = models.DateTimeField(verbose_name='直播开始时间')
    live_end_time = models.DateTimeField(verbose_name='直播结束时间')
    anchor = models.CharField(max_length=50, verbose_name='主播')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')


    class Meta:
        unique_together = ('item_id', 'live_start_time', 'live_end_time')
        verbose_name = '直播商品信息配置表'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']


class OutputRecord(models.Model):
    pass

    class Meta:
        verbose_name = '输出直播报告'
        verbose_name_plural = verbose_name