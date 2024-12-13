from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('chatbot/', TemplateView.as_view(template_name='index_change/chat.html')),
]