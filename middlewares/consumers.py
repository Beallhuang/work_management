import json
import time
from channels.generic.websocket import JsonWebsocketConsumer
from .models import OutputLogs, AccessTimeOutLogs

class OpLogsConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()
        self.start_time = time.time()
        self.data = dict()
        x_forwarded_for = self.scope["headers"].get(b"x-forwarded-for")
        re_ip = x_forwarded_for.decode().split(",")[0] if x_forwarded_for else self.scope["client"][0]

        self.data.update({
            're_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
            're_url': self.scope["path"],
            're_method': "WS",
            're_ip': re_ip,
            're_content': None,
            're_user': self.scope["user"].username if self.scope["user"].is_authenticated else 'AnonymousUser'
        })

    def receive_json(self, content, **kwargs):
        self.data['re_content'] = json.dumps(content)
        self.send_json(content)  # Just echo back the message for now

    def disconnect(self, close_code):
        self.data.update({
            'rp_content': None,  # Capture if there's any specific response content you want to store
        })
        self.end_time = time.time()
        access_time = self.end_time - self.start_time
        self.data['access_time'] = round(access_time * 1000)
        if self.data.get('access_time') > 3 * 1000:
            AccessTimeOutLogs.objects.create(**self.data)
        OutputLogs.objects.create(**self.data)