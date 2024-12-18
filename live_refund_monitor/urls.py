from django.urls import path
from .views import CommandView  # 导入自定义的视图

urlpatterns = [
    path('command/', CommandView.as_view(), name='command'),
]
