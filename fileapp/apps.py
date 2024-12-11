from django.apps import AppConfig


class FileappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fileapp'
    verbose_name = '文件管理'
    verbose_name_plural = '文件管理'
