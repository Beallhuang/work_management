from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import JDSZIndex, GradioProxy
from .views import jdsz_index_change_view

@admin.register(JDSZIndex)
class JDSZIndexAdmin(admin.ModelAdmin):
    pass

    def changelist_view(self, request, extra_content=None):
        return jdsz_index_change_view(request)
    
@admin.register(GradioProxy)
class GradioProxyAdmin(admin.ModelAdmin):
    pass

    def changelist_view(self, request, extra_content=None):
        return HttpResponseRedirect('/index_change/chatbot/')