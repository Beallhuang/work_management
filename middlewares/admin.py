from django.contrib import admin
from .models import OutputLogs, AdminUserLog, AccessTimeOutLogs
from django.contrib.admin.models import CHANGE, DELETION, ADDITION, LogEntry


@admin.register(AdminUserLog)
class AdminUserLogAdmin(admin.ModelAdmin):
    list_display = ('action_time', 'user', 'content_type', 'object_id', 'action_flag', 'change_message')
    list_filter = ('action_flag', 'user', 'content_type')
    search_fields = ('object_id', 'change_message')

    def action_flag(self, obj):
        """返回操作类型的可读字符串"""
        return dict(ADDITION= '添加', CHANGE='更改', DELETION='删除').get(obj.action_flag)

    def content_type(self, obj):
        """返回内容类型的名称"""
        return obj.content_type.model
    
    
@admin.register(OutputLogs)
class OutputLogsAdmin(admin.ModelAdmin):
    list_display = ('re_time','re_user','re_ip','re_url','re_method','re_content', 'access_time')
    list_filter = ('re_user','re_url','re_method')
    search_fields = ('re_content',)


@admin.register(AccessTimeOutLogs)
class AccessTimeOutLogsAdmin(admin.ModelAdmin):
    list_filter = ('re_time','re_user','re_ip','re_url','re_method', 're_content', 'access_time')
    search_fields = ('re_content',)