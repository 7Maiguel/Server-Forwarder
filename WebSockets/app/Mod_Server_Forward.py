from lib.Lib_WS import WebSocketFuseaccess
from lib.Lib_Settings import Get_Socket_Timeout, Get_Forward_server
from lib.Lib_Request_Json import send_petition
from operator import attrgetter
import time
import os


CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
socket_timeout = Get_Socket_Timeout()
server_to_forward = Get_Forward_server()


class WSServerForward(WebSocketFuseaccess):
    def on_message(self, msg):
        message = msg["message"]
        print(msg)
        response = send_petition(
            "http://192.168.0.103:4000"+message["url"], method=message["method"], json_data=message["data"], headers=message["headers"])
        if response:
            print(response.json())
            msg["response"]=response.json()
            self.send_message("get_response",msg)


ws = WSServerForward("ServerForwardChannel")


while True:
    ws.create_connection()
    time.sleep(socket_timeout)
    ws.close_connection()
