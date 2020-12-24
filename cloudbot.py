#!/usr/bin/python3

import requests
import os

URL = os.getenv('CLOUD_URL')
CHAT_ID = os.getenv('CHAT_ID')

def getUpdatesJson(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def lastUpdate(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def getChatId(update):
        chatId = update['message']['chat']['id']
        return chatId

def sendMessage(chat, text):
        params = {'chat_id': chat, 'text': text}
        response = requests.post(URL + 'sendMessage', data=params)
        return response

def sendPhoto(chat, photo):
        params = {'chat_id': chat, 'photo': photo}
        response = requests.post(URL + 'sendPhoto', data=params)
        return response

#chatId = getChatId(lastUpdate(getUpdatesJson(URL)))
#photo = 'https://i.forfun.com/jmta9hxs.jpeg'
message = 'Testing test '
message = 'Testing test '
sendMessage(CHAT_ID, message)
#sendPhoto(chatId, photo)
