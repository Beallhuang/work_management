from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.http import Http404, HttpResponse
import re

class PermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        # 登录检查
        if (not request.user.is_authenticated) and (not re.match(r'^/static/', request.path_info) 
                                                    # or not re.match(r'^/media/', request.path_info)
                                                    or not re.match(r'^/api/login/', request.path_info) 
                                                    or not re.match(r'^/admin/login/', request.path_info)):
            return redirect(self.login_url + '?next=' + request.path)
        
        # 权限检查    
        if re.search('upload', path) and not request.user.has_perm('fileapp.add_filemanage'):
            return HttpResponse('You do not have permission to upload files.')    
        if re.search('download', path) and not request.user.has_perm('fileapp.change_filemanage'):
            return HttpResponse('You do not have permission to download files.')    
        if re.search('delete', path) and not request.user.has_perm('fileapp.delete_filemanage'):
            return HttpResponse('You do not have permission to delete files.')   
             

        response = self.get_response(request)
        return response