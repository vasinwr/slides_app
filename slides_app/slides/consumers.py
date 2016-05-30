from channels import Group
from .models import Slides

'''
def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)
'''
def ws_message(message):
    print("echo here")
    Group("chat").send({
        "text": "[user] %s" % message.content['text'],
    })

# Connected to websocket.connect
def ws_add(message):
    print(message.reply_channel)
    Group("chat").add(message.reply_channel)

# Connected to websocket.disconnect
def ws_disconnect(message):
    print(message.reply_channel)
    Group("chat").discard(message.reply_channel)
