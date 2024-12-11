'''
Description: 
Author: beallhuang
Date: 2024-07-01 11:18:21
LastEditTime: 2024-07-01 13:31:56
LastEditors: beallhuang
'''
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.http import Http404, HttpResponse
import re

class PermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = '/admin/login/'
        self.open_urls = [self.login_url] + getattr(settings, 'OPEN_URLS', ['/static/', '/media/', '/api/login/'])

    def __call__(self, request):
        path = request.path

        # 登录检查
        if (not request.user.is_authenticated) and (request.path_info not in self.open_urls):
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
    
import logging

# 创建一个日志记录器
logger = logging.getLogger(__name__)

class DetailedLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 获取用户信息
        user = request.user if request.user.is_authenticated else 'Anonymous'
        ip_address = self.get_client_ip(request)

        # 在请求开始时记录日志
        logger.info(
            f"Request Method: {request.method}, Request Path: {request.path}, "
            f"User: {user}, IP Address: {ip_address}"
        )

        response = self.get_response(request)

        # 在请求结束时记录日志
        logger.info(
            f"Response Status Code: {response.status_code}, User: {user}, IP Address: {ip_address}"
        )

        return response

    def get_client_ip(self, request):
        """获取客户端的 IP 地址"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip