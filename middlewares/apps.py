from django.apps import AppConfig


class MiddlewaresConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "middlewares"
    verbose_name = "用户访问日志"
    verbose_name_plural = verbose_name
