from channels.routing import route
from slides.consumers import ws_message

channel_routing = [
    route("websocket.receive", ws_message),
]
