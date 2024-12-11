from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.directory_list, name='directory_list'),
    path('files/<int:directory_id>/', views.file_list, name='file_list'),
    re_path(r'^files/(?P<directory_id>\d+)(?:/(?P<sub_path>.*))?/$', views.file_list, name='file_list_subpath'),
    path('files/upload/<int:directory_id>/', views.file_upload, name='file_upload'),
    path('files/upload/<int:directory_id>/<path:sub_path>/', views.file_upload, name='file_upload_subpath'),
    path('files/download/<path:file_path>/', views.file_download, name='file_download'),
    path('file/view/<path:file_path>/', views.file_view, name='file_view'),
    re_path(r'^files/(?P<directory_id>\d+)/delete/(?P<sub_path>.+)$', views.file_delete, name='file_delete_subpath'),
]