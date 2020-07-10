from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage
)


app = Flask(__name__)

line_bot_api = LineBotApi('b6EaTtzpXIHVJ1yiTWjvHvAClDSD9DaN7s4s/5OGrO85efGG+aQLEFidQzyH1vqoVnmBcs15oxhwLJxrhyvP5Be92L+FZQPZhdi6x3bcDiWl0Ug893ch0gj8aUr+Ru9WJkucxlNE75ZbI37aHn5XiwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0d3b0de5b0284c15db10e4244fd46340')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@app.route("/new", methods=['POST'])


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我看不懂你說甚麼?'

    if '圖片' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://cdn.hk01.com/di/media/images/3023738/org/67df85b6f7f06a7624bed0dd5f1f6afa.jpg/WRIzIxRqUxud42IOEObM_e9aHf1qKAWlokR5eqJEeXo?v=w1280.png',
            preview_image_url='https://cdn.hk01.com/di/media/images/3023738/org/67df85b6f7f06a7624bed0dd5f1f6afa.jpg/WRIzIxRqUxud42IOEObM_e9aHf1qKAWlokR5eqJEeXo?v=w1280.png')
        
        line_bot_api.reply_message(
        event.reply_token,
        image_message)

        return    



    if '貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='2',sticker_id='23')
        
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)

        return

    if 'hi' in msg:
        r = 'hi'
    elif '你吃飯了嗎' in msg:
        r = '還沒'
    elif '你是誰' in msg:
        r = '我是line bot'
    elif '訂位' in msg:
        r = '請問您想訂位的時間?'
    


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))

if __name__ == "__main__":
    app.run()






