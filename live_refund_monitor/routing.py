from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/command/', consumers.CommandConsumer.as_asgi()),
]