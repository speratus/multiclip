import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.conf import settings

import redis


class ClipConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            host = settings.CHANNEL_LAYERS['default']['CONFIG']['hosts'][0]
        except AttributeError:
            raise ValueError(
                "Must set a CHANNEL_LAYERS attribute in settings as per the channels docs"
            )
        self.store = redis.Redis(host=host[0], port=host[1], db=0)

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

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

        if 'update' in text_data_json:
            group_board = self.store.get(self.clipboard_id)
            if group_board is not None:
                board = group_board.decode('utf-8')
                self.send(text_data=json.dumps({
                    'clipboard': board
                }))
            return

        clipboard = text_data_json['clipboard']
        self.store.set(self.clipboard_id, clipboard)

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
