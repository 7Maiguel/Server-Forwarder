from lib.Lib_WS import WebSocketFuseaccess
from lib.Lib_Settings import SERVER_TO_FORWARD, SOCKECTS_TIMEOUT
from lib.Lib_Request_Json import send_petition
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
next_reconection_time = time.time() + SOCKECTS_TIMEOUT
ws.create_connection()
while True:
    try:
        time.sleep(10)
        if ws.connection and ws.connection.connected and ws.subscription:
            time_now = time.time()
            if time_now > next_reconection_time:
                ws.close_connection()
                next_reconection_time = time_now + SOCKECTS_TIMEOUT
        else:
            ws.create_connection()
    except Exception as e:
        print(e)
