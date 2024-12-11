from django.contrib import admin
from .models import Directory, FileManage
from .views import directory_list


# 设置站点管理后台标题
admin.site.site_header = '后台管理系统'
admin.site.site_title = '后台管理系统'
admin.site.index_title = '后台管理系统'

@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'path')
    filter_horizontal = ('users',)  # Enables a nicer UI for the many-to-many field

@admin.register(FileManage)
class FileManageAdmin(admin.ModelAdmin):
    pass

    def changelist_view(self, request, extra_content=None):
        return directory_list(request)
