# consumers.py
from django.http import HttpResponse
from channels.handler import AsgiHandler
import json
from channels import Channel, Group
from channels.sessions import channel_session
from urllib.parse import parse_qs

from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
from ccp.models import IFD_POST_DATA_M, TOTAL_SEQ_INFO_M
import datetime, time


# http.request 기본
# def http_consumer(message):
#     # Make standard HTTP response - access ASGI path attribute directly
#     response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
#     # Encode that response into message format (ASGI)
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)
#


# Connected to websocket.connect
def ws_connect(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # print('[ID] : {}'+id)
    # Add to the chat group
    # Group("id").add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    print('temp : %s' %message.content)
    temp_id = message.content["path"]
    temp_id = temp_id.replace('/','')
    temp_text = message.content["text"]
    print('temp_id : %s' % temp_id)
    print('temp_text : %s' %temp_text)

    #send_message = 'CCP DATA STRING'
    # check the TOTAL_SEQ_INFO_M table

    if temp_id :
        #for i in range(1, 10):
           # 개별 송신
           # message.reply_channel.send({
           #   "text": "[{}] {}".format(i, send_message)
           # })
           # group send
           # Group("id").send({
           #     "text": "%s [{}]".format(i) % send_message,
           # })
           #

            # IFD_POST_DATA_M 데이타 송신
            rows = ''
            qs = IFD_POST_DATA_M.objects.filter(member = temp_id)
            if qs:
                    for item in qs:
                        rows = rows + \
                               'Date:' + str(item.created_at) + ',' + \
                               'Market:' + item.market + ',' + \
                               'Product:' + item.product + ',' + \
                               'Member:' + item.member + ',' + \
                               'Item:' + item.item + ',' + \
                               'Item_Group:' + item.item_group + ',' + \
                               'Item_Seq:' + item.item_seq + ',' + \
                               'Data:' + item.data + ','

                    for i in range(1,1000):
                        message.reply_channel.send({
                       "text": " {}".format(json.dumps(rows))
                     })

    else :
                print ('Else rutin')


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("id").discard(message.reply_channel)



# # USER 값을 입력받아 세션 유지
# # # Connected to websocket.connect
# import json
# from urllib import parse
#
# from channels import Group
# from channels.sessions import channel_session
#
#
# @channel_session
# def ws_add(message, room):
#     print('room = '+room)
#     query = parse.parse_qs(message['query_string'])
#     if 'username' not in query:
#         return
#     Group('chat-%s' % room).add(message.reply_channel)
#     message.channel_session['room'] = room
#     message.channel_session['username'] = query['username'][0]
#     print('ws_add')
#
# @channel_session
# def ws_echo(message):
#     if 'username' not in message.channel_session:
#         return
#     room = message.channel_session['room']
#     Group('chat-%s' % room).send({
#         'text': json.dumps({
#             'message': message.content['text'],
#             'username': message.channel_session['username']
#         }, ensure_ascii=False),
#     })