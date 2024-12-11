from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('command/', TemplateView.as_view(template_name='live_refund_monitor/command.html')),
]