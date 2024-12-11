'''
Description: 
Author: beallhuang
Date: 2024-06-28 17:50:08
LastEditTime: 2024-07-01 11:21:17
LastEditors: beallhuang
'''
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('files/', include('files.urls')),
    path('index_change/', include('index_change.urls')),  
    path('fileapp/', include('fileapp.urls')),
    path('industry_report_upload/', include('industry_report_upload.urls')),
    path('live_refund_monitor/', include('live_refund_monitor.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), 
                    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]