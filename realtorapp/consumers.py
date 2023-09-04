# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import *
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from datetime import datetime



class ChatConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def save_message(self , sender_name , sender_id , reciver_name , reciver_id , message):
        sender = profile.objects.get(id = sender_id , f_name = sender_name)
        reciver = profile.objects.get(id = reciver_id , f_name = reciver_name)
        chat_mesage = saved_message(
            sender = sender,
            reciver = reciver ,
            message = message , 
            time_stamp = datetime.now()
        )
        chat_mesage.save()
    @database_sync_to_async
    def change_user_status(self , user , status):
        profile_user =  profile.objects.get(user=user)
        profile_user.status = status
        profile_user.save()
        print('done')

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        user = self.scope['user']
        print('connected')
        await self.change_user_status(user, 'online')
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        user = self.scope['user']
        print('disconnected')
        await self.change_user_status(user, 'offline')


    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        reciver_name = data['reciver_name']
        reciver_id = data['reciver_id']
        sender_name = data['sender_name']
        sender_id = data['sender_id']

        await self.save_message(sender_name, sender_id, reciver_name, reciver_id, message)


        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'reciver_name':reciver_name ,
                'reciver_id':reciver_id,
                'sender_name':sender_name,
                'sender_id':sender_id,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        reciver_name = event['reciver_name']
        reciver_id = event['reciver_id']
        sender_name = event['sender_name']
        sender_id = event['sender_id']
        await self.send(text_data=json.dumps({
            'message': message ,
            'reciver_name':reciver_name ,
            'reciver_id':reciver_id,
            'sender_name':sender_name,
            'sender_id':sender_id
        }))
        # await ChatConsumer.save_message(sender_name , sender_id , reciver_name , reciver_id , message)
