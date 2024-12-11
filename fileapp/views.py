import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest, FileResponse, HttpResponse
from .models import Directory
from django.conf import settings


def directory_list(request):
    directories = Directory.objects.filter(users=request.user)
    return render(request, 'fileapp/directory_list.html', {'directories': directories})


def get_directory_contents(directory_path):
    contents = []
    if not os.path.exists(directory_path):
        raise Http404(f"Directory path {directory_path} does not exist")
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            contents.append({
                'name': item,
                'type': 'directory',
                'path': item_path
            })
        elif os.path.isfile(item_path) and item_path.endswith(('.html', '.txt', '.jpg', '.jpeg', '.png', '.log')):
            contents.append({
                'name': item,
                'type': 'open_able',
                'path': item_path
            })
        else:
            contents.append({
                'name': item,
                'type': 'file',
                'path': item_path
            })
    return contents


def normalize_path(directory_path, sub_path):
    print(f'''normalize_path: directory_path={directory_path}, sub_path={sub_path}''')
    return os.path.normpath(os.path.join(directory_path, sub_path))


def file_list(request, directory_id, sub_path=''):
    try:
        directory = Directory.objects.get(pk=directory_id, users=request.user)
    except Directory.DoesNotExist:
        raise Http404("Directory does not exist")

    current_path = normalize_path(directory.path, sub_path)
    directory_contents = get_directory_contents(current_path)
    # print(f'''file_list: current_path={current_path}, directory_contents={directory_contents}''')

    return render(request, 'fileapp/file_list.html', {
        'directory': directory,
        'contents': directory_contents,
        'sub_path': sub_path,
        'current_path': current_path
    })


def file_upload(request, directory_id, sub_path=''):
    try:
        directory = Directory.objects.get(pk=directory_id, users=request.user)
    except Directory.DoesNotExist:
        raise Http404("Directory does not exist")

    current_path = normalize_path(directory.path, sub_path)

    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        upload_path = os.path.join(current_path, file.name)
        with open(upload_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return redirect('file_list_subpath', directory_id=directory_id, sub_path=sub_path)

    return render(request, 'fileapp/file_upload.html', {'directory': directory, 'sub_path': sub_path, 'current_path': current_path})


def file_delete(request, directory_id, sub_path=''):
    try:
        directory = Directory.objects.get(pk=directory_id, users=request.user)
    except Directory.DoesNotExist:
        raise Http404("Directory does not exist")

    file_path = normalize_path(directory.path, sub_path)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        os.remove(file_path)
    else:
        return HttpResponseBadRequest("File does not exist or is not a file")

    parent_sub_path = os.path.dirname(sub_path)
    return redirect('file_list_subpath', directory_id=directory_id, sub_path=parent_sub_path)


def file_download(request, file_path):
    if not os.path.exists(file_path):
        raise Http404("File not found")
    
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_path.split('/')[-1])


def file_view(request, file_path):
    # 检查文件是否存在
    if not os.path.exists(file_path):
        raise Http404("File not found")

    # 获取文件扩展名
    file_extension = os.path.splitext(file_path)[1].lower()

    # 如果是HTML或TXT文件，直接返回文件内容
    if file_extension in ['.html', '.txt']:
        return HttpResponse(open(file_path, 'r', encoding='utf-8').read(), content_type='text/plain' if file_extension == '.txt' else 'text/html')
    elif file_extension == '.log':
        return HttpResponse(open(file_path, 'r', encoding='utf-8').read(), content_type='text/plain;charset=utf-8')
    elif file_extension in ['.jpg', '.jpeg', '.png']:
        return HttpResponse(open(file_path, 'rb').read(), content_type='image/jpeg' if file_extension == '.jpg' else 'image/png')

    # 如果是其他类型的文件，返回一个下载链接
    else:
        return HttpResponse(f'<a href="/file/download/{file_path}">Download {file_path}</a>')


        
