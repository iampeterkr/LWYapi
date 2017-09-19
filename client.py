from websocket import create_connection
ws = create_connection("ws://localhost:8002/00001")
print("Sending 'IRS_WON, 00001'")
ws.send("product : IRS_WON, member: 00001")
print("Sent ok ")
print("Receiving...")
while 1:
    result =  ws.recv()
    print("Received :  '%s'" % result)
ws.close()

