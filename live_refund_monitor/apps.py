from django.apps import AppConfig


class LiveRefundMonitorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "live_refund_monitor"
    verbose_name = '直播退货分析'
    verbose_name_plural = '直播退货分析'
