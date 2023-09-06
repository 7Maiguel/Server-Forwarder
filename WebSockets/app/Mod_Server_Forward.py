from lib.Lib_WS import WebSocketFuseaccess
from lib.Lib_Settings import CENTRALIZER_SERVER, SERVER_TO_FORWARD, SOCKECTS_TIMEOUT
from lib.Lib_Request_Json import send_petition
from operator import attrgetter
import time
import os


CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class WSServerForward(WebSocketFuseaccess):
    def on_message(self, msg):
        message = msg["message"]
        response = send_petition(
            SERVER_TO_FORWARD + message["url"],
            method=message["method"],
            json_data=message["data"],
            headers=message["headers"]
        )
        if response:
            msg["response"] = response.json()
            self.send_message("get_response", msg)


ws = WSServerForward("ServerForwardChannel")


while True:
    ws.create_connection()
    time.sleep(SOCKECTS_TIMEOUT)
    ws.close_connection()
