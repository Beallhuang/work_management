from django.urls import path
from . import views

urlpatterns = [
    # 其他路由
    path('get_image_url/<int:pk>/', views.get_image_url, name='get_image_url'),
]