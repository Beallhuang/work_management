from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import UploadFileTemplate

def get_image_url(request, pk):
    # 根据主键获取对象
    obj = get_object_or_404(UploadFileTemplate, pk=pk)

    import requests
    import sys 
    import socket

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    sys.path.append("/home/huang.biao/anaconda3/lib/python3.9/site-packages/base_function") 
    from generate_date import get_last_date, get_last_sunday, get_range_month, get_last_monday

    if obj.report_type == 'daily':
        cover_date = get_last_date()
    elif obj.report_type == 'weekly':
        cover_date = get_last_monday() + '~' + get_last_sunday()
    elif obj.report_type == 'monthly':
        cover_date = get_range_month()[0] + '~' + get_range_month()[1]
    else:
        cover_date = get_last_date()

    url = f"http://{local_ip}:8756/get_cover_image_url?template_page={obj.template_page}&date={cover_date}&title={obj.title}"
    image_url = requests.get(url).json()

    # 获取图片 URL（可以通过模型的自定义方法生成）
    if image_url:
        return JsonResponse({'image_url': image_url})
    return JsonResponse({'error': 'No image found'}, status=404)