import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ClipConsumer(WebsocketConsumer):
    def connect(self):
        self.clipboard_id = self.scope['url_route']['kwargs']['clipboard_id']
        self.room_group_name = f'clipboard_{self.clipboard_id}'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        user = self.scope['user']
        if user.userclipboard.clipboard_id == self.clipboard_id:
            self.accept()
            clipboard = user.userclipboard
            if clipboard.current_item != '':
                self.send(text_data=json.dumps({
                    'clipboard': clipboard.current_item
                }))

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
        user = self.scope['user']
        user_clipboard = user.userclipboard
        user_clipboard.current_item = clipboard
        self.send(text_data=json.dumps({
            'clipboard': clipboard
        }))
