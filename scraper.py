from websocket import create_connection
import threading
import time, json

BASE_URL = "wss://api.rbxgold.com/socket.io/?EIO=4&transport=websocket"
PUT_MSG_IN_FILE = False

# MADE BY COXY
# MADE BY COXY
# MADE BY COXY
# MADE BY COXY
# MADE BY COXY
# MADE BY COXY
# MADE BY COXY


x = "madebycoxy57"
y = "madebycoxy57"
z = "madebycoxy57"

ws = create_connection(BASE_URL)
ws.send('40')

def messagescraperHandler():
    if not all(v in globals() for v in ("x","y","z")): return False
    time.sleep(0.5)
    ws.send('42["chat-join","general"]')
    while True:
        msg = str(ws.recv())
        if "chat-stream" in msg:
            chat_stream_dict = json.loads(msg.split('chat-stream",')[1].rstrip(']'))
            documents = [(v['text'],v['senderName']) for v in chat_stream_dict['documents'] if not v['senderName'] == "Case Battles" and not v['senderName'] == "Rewards"]
            if not all(v in globals() for v in ("x", "y", "z")): return False
            for document in documents:
                print('%s: %s' % (document[1],document[0]))
            if PUT_MSG_IN_FILE:
                w = open('msgs.txt','a+')
                for document in documents:
                    text = str(document[0])
                    senderName = document[1]
                    w.write('%s: %s\n' % (senderName,text))
        elif "2" == msg:
            ws.send("3")
        else:
            pass


threading.Thread(target=messagescraperHandler).start()



# MADE BY COXY
# MADE BY COXY
# MADE BY COXY
# MADE BY COXY
# MADE BY COXY
# MADE BY COXY
# MADE BY COXY
