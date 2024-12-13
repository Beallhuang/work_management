import json
import os
from channels.generic.websocket import AsyncWebsocketConsumer
import openai
from openai import OpenAI
from django.conf import settings
openai.api_key = os.getenv('OPENAI_API_KEY')
# openai.api_key = 'sk-JSGqHabFGLLqpe7t91Ee2aE58f4548E080E9D81d900802F5'


client = OpenAI(api_key=settings.OPENAI_API_KEY, base_url=settings.OPENAI_API_URL)

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model='gpt-4o',
        messages=history_openai_format,
        temperature=1.0,
        stream=True
    )

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta and chunk.choices[0].delta.content:
            partial_message += chunk.choices[0].delta.content
            yield partial_message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_history = []
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        self.chat_history.append((message, ""))  # Add user message with empty response initially
        
        try:
            chunks = predict(message, self.chat_history)
            
            partial_message = ""
            async for chunk in self.async_stream_message(chunks):
                partial_message = chunk
                self.chat_history[-1] = (message, partial_message)
                await self.send(text_data=json.dumps({'response': partial_message}))
        
        except Exception as e:
            await self.send(text_data=json.dumps({'error': str(e)}))

    async def async_stream_message(self, chunks):
        for chunk in chunks:
            yield chunk