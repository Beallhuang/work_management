"""
ASGI config for belle_management project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path, re_path
from live_refund_monitor.consumers import CommandConsumer
from index_change.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'belle_management.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                re_path(r'ws/chatbot/$', ChatConsumer.as_asgi()),
                re_path(r'ws/command/$', CommandConsumer.as_asgi()),
            ]
        )
    ),
})
