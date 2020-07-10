from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, FlexSendMessage
)


app = Flask(__name__)

line_bot_api = LineBotApi('b6EaTtzpXIHVJ1yiTWjvHvAClDSD9DaN7s4s/5OGrO85efGG+aQLEFidQzyH1vqoVnmBcs15oxhwLJxrhyvP5Be92L+FZQPZhdi6x3bcDiWl0Ug893ch0gj8aUr+Ru9WJkucxlNE75ZbI37aHn5XiwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0d3b0de5b0284c15db10e4244fd46340')

def flex():
    return FlexSendMessage('Hello world',{
    "type": "bubble",
    "hero": {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "uri": "http://linecorp.com/"
                }
              },
              "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Brown Cafe",
                    "weight": "bold",
                    "size": "xl"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "md",
                    "contents": [
                      {
                        "type": "icon",
                        "size": "sm",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                      },
                      {
                        "type": "icon",
                        "size": "sm",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                      },
                      {
                        "type": "icon",
                        "size": "sm",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                      },
                      {
                        "type": "icon",
                        "size": "sm",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                      },
                      {
                        "type": "icon",
                        "size": "sm",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                      },
                      {
                        "type": "text",
                        "text": "4.0",
                        "size": "sm",
                        "color": "#999999",
                        "margin": "md",
                        "flex": 0
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Place",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 1
                          },
                          {
                            "type": "text",
                            "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                            "wrap": True  ,
                            "color": "#666666",
                            "size": "sm",
                            "flex": 5
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Time",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 1
                          },
                          {
                            "type": "text",
                            "text": "10:00 - 23:00",
                            "wrap": True  ,
                            "color": "#666666",
                            "size": "sm",
                            "flex": 5
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                      "type": "uri",
                      "label": "CALL",
                      "uri": "https://linecorp.com"
                    }
                  },
                  {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                      "type": "uri",
                      "label": "WEBSITE",
                      "uri": "https://linecorp.com"
                    }
                  },
                  {
                    "type": "spacer",
                    "size": "sm"
                  }
                ],
                "flex": 0
              }
            })






@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True  )
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'




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
    
    if 'cafe' in msg:
    	flex_message = flex()
    	line_bot_api.reply_message(
        event.reply_token,
        flex_message)
if __name__ == "__main__":
    app.run()






