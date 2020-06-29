import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ClipConsumer(WebsocketConsumer):
    def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['clipboard_id']
        self.room_group_name = f'clipboard_{self.room_id}'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        clipboard = text_data_json['clipboard']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'update_clipboard',
                'clipboard': clipboard
            }
        )

    def update_clipboard(self, event):
        clipboard = event['clipboard']

        self.send(text_data=json.dumps({
            'clipboard': clipboard
        }))