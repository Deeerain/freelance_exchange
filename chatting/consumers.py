import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatRoomConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.chat_box_name = self.scope['url_route']['kwargs']['chat_box_name']
        self.group_name = 'chat_%s' % self.chat_box_name

        await self.channel_layer.group_add(self.group_name, self.channel_name)  

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name,
                                               self.channel_name)

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chatbox_message',
                'message': message,
                'username': username,
            }
        )

    async def chatbox_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(
            text_data=json.dumps({
                'message': message,
                'username': username,
            })
        )
