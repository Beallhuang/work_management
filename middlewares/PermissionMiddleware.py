from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.http import Http404, HttpResponse
import re

class PermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = reverse('admin:login')  # 使用 Django 提供的 reverse 方法来获取登录 URL
        self.open_urls = [
            self.login_url,
            reverse('admin:logout'),
        ] + getattr(settings, 'OPEN_URLS', ['/static/', '/media/'])

    def __call__(self, request):
        path = request.path

        # 静态文件等特殊路径处理
        if any(re.match(url, path) for url in self.open_urls):
            return self.get_response(request)

        # 登录检查
        if not request.user.is_authenticated:
            return redirect(f'{self.login_url}?next={path}')
        
        # 权限检查    
        if re.search('fileapp.*upload', path) and not request.user.has_perm('fileapp.add_filemanage'):
            return HttpResponse('You do not have permission to upload files.')    
        if re.search('fileapp.*download', path) and not request.user.has_perm('fileapp.change_filemanage'):
            return HttpResponse('You do not have permission to download files.')    
        if re.search('fileapp.*delete', path) and not request.user.has_perm('fileapp.delete_filemanage'):
            return HttpResponse('You do not have permission to delete files.')   

        response = self.get_response(request)
        return response