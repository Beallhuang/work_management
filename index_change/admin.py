from django.contrib import admin
from .models import JDSZIndex
from .views import jdsz_index_change_view

@admin.register(JDSZIndex)
class FileManageAdmin(admin.ModelAdmin):
    pass

    def changelist_view(self, request, extra_content=None):
        return jdsz_index_change_view(request)