from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class NotifyConsumer(WebsocketConsumer):
    def connect(self):
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            "g1",
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            "g1",
            self.channel_name
        )
