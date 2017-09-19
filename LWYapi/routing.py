# routing.py
from channels.routing import route
# app 밑에 consumers 사용
from channels.routing import route

# channel_routing = [
    # chat = app name
    #route("http.request", "chat.consumers.http_consumer"),

    # Basic websocket
    #      route("websocket.connect" , ws_add) ,
    #      route("websocket.receive" , ws_message) ,
#         route("websocket.disconnect" , ws_disconnect) ,
# ]

    # websocket 사용시- 변수 읽기
    # 아래와 같이 import 하지 않고 chat의 consumers의 ws_echo 함수를 사용한다고 명시할수있다
    #route('websocket.receive', 'chat.consumers.ws_echo'),
# ]

# in routing.py
from channels.routing import route
from chat.consumers import ws_connect, ws_message, ws_disconnect

channel_routing = [
    # 입력값 존재
    # route("websocket.connect" , ws_connect , path=r'^/(?P<room_name>[a-zA-Z0-9_]+)/$') ,
    # route("websocket.receive" , ws_message, path=r'^/(?P<room_name>[a-zA-Z0-9_]+)/$') ,
    # route("websocket.disconnect" , ws_disconnect, path=r'^/(?P<room_name>[a-zA-Z0-9_]+)/$') ,

    route("websocket.connect" , ws_connect ) ,
    # route("websocket.connect" , ws_connect, path=r'^/(?P<id>a-zA-Z0-9_]+)/$' ) ,
    route("websocket.receive" , ws_message) ,
    route("websocket.disconnect" , ws_disconnect) ,

    #
    # route("websocket.connect", ws_add, path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    # route("websocket.receive", ws_echo, path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),

]
