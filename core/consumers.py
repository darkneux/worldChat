import json

from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from time import sleep

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("WebSocket Connected...",event)
        print("Channel Layer : ",self.channel_layer)
        print("Channel Name : ", self.channel_name)
        group_name =  self.scope['url_route']['kwargs']['group_name']  # because in views we can easily call in function parameter for dynamic url
        print("Group Name : ", group_name)
        async_to_sync (self.channel_layer.group_add)(group_name,self.channel_name)
        self.send({
            'type': 'websocket.accept',
            # 'text': "hello bitch"

        })

    def websocket_receive(self,event):
        print("WebSocket Connected...",event)
        group_name = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_send)(group_name, {
            'type': 'chat.message',
            'message': event['text']
        })

    def chat_message(self,event):
        print(event)
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })


    def websocket_disconnect(self,event):
        print("WebSocket Disconnected...",event)
        group_name = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_discard)(group_name, self.channel_name)
        raise StopConsumer()





class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print("WebSocket Connected...",event)
        print("Channel Layer")
        await self.send({
            'type':'websocket.accept',
             'text':'hello bitch'

        })

    async def websocket_receive(self,event):
        await self.send(
            {
                'type':'websocket.send',
                 'text':'hello bitch'
            }
        )

    async def websocket_disconnect(self,event):
        print("WebSocket Disconnected...",event)
        raise StopConsumer()
