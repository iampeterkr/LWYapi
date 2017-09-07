# routing.py
from channels.routing import route

# channel_routing = [
#     route('websocket.receive', 'chat.consumers.ws_echo'),
# ]

channel_routing = [
    # chat = app name
    route("http.request", "chat.consumers.http_consumer"),
]
