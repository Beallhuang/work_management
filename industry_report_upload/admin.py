from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from .models import UploadFileTemplate, CoverImageTemplate


@admin.register(UploadFileTemplate)
class UploadFileTemplateAdmin(admin.ModelAdmin):
    actions = ['upload_files']

    @admin.action(description='开始手动上传报告')
    def upload_files(self, request, queryset):
        # 从queryset中取出id，并拼接成命令行参数
        ids = ','.join(str(i.id) for i in queryset)
        params = f"/home/huang.biao/anaconda3/bin/python /home/huang.biao/anaconda3/lib/python3.9/site-packages/base_function/industry_report_center/main.py --ids {ids}"
        return HttpResponseRedirect(f'/live_refund_monitor/command/?run_param={params}')

    # 显示字段
    @admin.display(description='封面图模板')
    def image(self, obj):

        return format_html('<img src="{}" border=0 width="100px" height="100px"/>',
                           obj.template_page.image_path.url) if obj.template_page else ''
    
    @admin.display(description='封面图预览')
    def preview_button(self, obj):
        return format_html(
                    '<button type="button" class="preview-btn" data-id="{}">预览</button>',
                    obj.id
                )


    class Media:
        css = {
            'all': ('industry_report_upload/custom.css',)  # 自定义 CSS 文件
        }
        js = ('industry_report_upload/custom.js',)  # 自定义 JS 文件
 
    autocomplete_fields = ('template_page',)
    list_display = ['dir_path', 'template_page', 'preview_button','title','report_type','report_tag', 'if_to_wps', 'is_active', 'create_time', 'update_time']
    list_display_links = ('dir_path',)
    list_filter = ('dir_path', 'report_type', 'report_tag', 'platform')
    search_fields = ('template_page', 'title')
    ordering = ('-update_time',)
    #  设置页面可直接编辑的字段
    list_editable = ('template_page', 'title','report_type','report_tag', 'if_to_wps', 'is_active')
    readonly_fields = ('create_time', 'update_time')


@admin.register(CoverImageTemplate)
class CoverImageTemplateAdmin(admin.ModelAdmin):

    @admin.display(description='商品图片')
    def image(self, obj):
        return format_html('<img src="{}" border=0 width="300px" height="160px"/>', obj.image_path.url) if obj.image_path else ''
    
    list_display = ['template_page_id', 'image', 'title_x', 'title_y', 'title_font_size', 'title_font_color', 'date_x', 'date_y', 'date_font_size', 'date_font_color', 'create_time', 'update_time']
    list_display_links = ('template_page_id',)
    search_fields = ('template_page_id',)
    ordering = ('-update_time',)
    #  设置页面可直接编辑的字段
    readonly_fields = ('create_time', 'update_time')