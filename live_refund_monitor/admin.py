from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from .models import ItemInfoLive, OutputRecord
from django.template.response import TemplateResponse

# Register your models here.
@admin.register(ItemInfoLive)
class ItemInfoLiveAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'brand_name', 'activity_name', 'commodity_desc', 'commodity_style_no', 'commodity_no', 'item_id', 'live_start_time', 'live_end_time', 'anchor', 'create_time', 'update_time']
    search_fields = ('item_id', 'activity_name', 'anchor')
    list_filter = ('brand_name', 'activity_name', 'anchor', 'live_start_time', 'live_end_time')
    ordering = ('-create_time',)
    readonly_fields = ('create_time', 'update_time')


@admin.register(OutputRecord)
class OutputRecordAdmin(admin.ModelAdmin):
    
    def changelist_view(self, request, extra_context = ...):
        params = "cd /home/huang.biao/jupyter_data/refund_monitor/python && /home/huang.biao/anaconda3/bin/python refund_monitor_tm_item_multiply_v241128.py"
        return HttpResponseRedirect(f'/live_refund_monitor/command/?run_param={params}')