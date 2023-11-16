from actioncable.connection import Connection
from actioncable.subscription import Subscription
from actioncable.message import Message
# import websocket
from lib.Lib_Settings import CENTRALIZER_SERVER, CHANEL_UUID, WSS_CENTRALIZER_SERVER


class WebSocketFuseaccess():

    def __init__(self, channel):
        print(self)
        print(channel)
        url = CENTRALIZER_SERVER
        ws_url = WSS_CENTRALIZER_SERVER
        self.ws_url = ws_url
        self.uuid = CHANEL_UUID
        self.channel = channel

    def create_connection(self):
        url = CENTRALIZER_SERVER
        ws_url = WSS_CENTRALIZER_SERVER
        print(ws_url)
        # connection = Connection(url=self.ws_url)
        connection = Connection(url=ws_url, origin=url)
        # connection = websockets.connect(ws_url)
        print(connection)
        connection.connect()
        print(connection.connect())
        print(self.channel)
        print(self.uuid)
        subscription = Subscription(connection,
                                    identifier={
                                        'channel': self.channel, 'uuid': self.uuid}
                                    )
        print(subscription)
        subscription.on_receive(callback=self.on_message)
        subscription.create()
        self.connection = connection
        self.subscription = subscription

    def close_connection(self):
        if self.connection and self.subscription:
            self.subscription.remove()
            self.connection.disconnect()
            self.subscription = None
            self.connection = None

    def send_message(self, action, data):
        if self.connection and self.subscription:
            message = Message(action=action, data=data)
            self.subscription.send(message)
            return True

    def on_message(self, msg):
        pass
