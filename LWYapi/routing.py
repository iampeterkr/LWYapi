# routing.py
from channels.routing import route
# app 밑에 consumers 사용
from chat.consumers import ws_message

# channel_routing = [

# ]

channel_routing = [
    # chat = app name
    #route("http.request", "chat.consumers.http_consumer"),

    # websocket 사용시
    route("websocket.receive", ws_message),
    # 아래와 같이 import 하지 않고 chat의 consumers의 ws_echo 함수를 사용한다고 명시할수있다
    #route('websocket.receive', 'chat.consumers.ws_echo'),
]
