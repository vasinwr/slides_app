from channels import Group

#connected to websocket.connect channel
def ws_add(message):
    print("ws_add called")
    Group("all").add(message.reply_channel)

#connected tp websocket.disconnect channel
def ws_disconnect(message):
    Group("all").discard(message.reply_channel)

