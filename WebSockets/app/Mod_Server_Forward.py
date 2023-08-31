from lib.Lib_WS import WebSocketFuseaccess
from lib.Lib_Settings import Get_Socket_Timeout, Get_Forward_server
from lib.Lib_Request_Json import send_petition
import time
import os


CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
socket_timeout = Get_Socket_Timeout()
server_to_forward = Get_Forward_server()


class WSServerForward(WebSocketFuseaccess):
    def on_message(self, msg):
        message = msg["message"]
        # send_petition()
        print(message)


ws = WSServerForward("ServerForwardChannel")


while True:
    ws.create_connection()
    time.sleep(socket_timeout)
    ws.close_connection()
