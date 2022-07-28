# LINE 聊天機器人的基本資料


from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi('6gOQ5E/06+dqkzAUAqoP7tvHNVHRAuaiX5ZFyA9pGOEOGPw0nyuN90ARUvZa7KLzeJJxClkL08A4cc96PLDe8PB9ENoJt+yk5YKe9eXLYBE/vtbrEOWLK4z3Z1TlZlkuEc/OLVE+kvVeeTiqCXDLSwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('678c31199ad1c9ed93f3339d8f3c72fa')

#   接收 LINE 的資訊
user_id='1657339819'
@app.route('/push_function/<string:push_message>')
def push_message(push_message):
    line_bot_api.push_message(user_id,TextSendMessage(text=push_message))


if __name__ == "__main__":
    app.run()
