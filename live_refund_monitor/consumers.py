import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import subprocess
from urllib.parse import unquote

class CommandConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()  # 接受 WebSocket 连接

    async def disconnect(self, close_code):
        pass  # 处理连接断开

    async def receive(self, text_data):
        # 接收到客户端消息，运行 Linux 命令
        command = unquote(text_data.strip())
        print(f'Received command: {command}')
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        # 实时读取输出并发送到前端
        while True:
            line = await process.stdout.readline()
            if not line:
                break
            await self.send(line.decode('utf-8'))  # 将输出实时发送到前端

        # 等待进程结束并获取返回码
        return_code = await process.wait()
        await self.send(f'Command finished with exit code {return_code}')