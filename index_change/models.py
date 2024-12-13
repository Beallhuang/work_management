from django.db import models

class JDSZIndex(models.Model):
    pass

    class Meta:
        verbose_name = '京东商智指数转化'
        verbose_name_plural = '京东商智指数转化'


class GradioProxy(models.Model):
    pass

    class Meta:
        managed = False
        verbose_name = 'chatbot'
        verbose_name_plural = verbose_name