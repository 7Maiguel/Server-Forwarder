from actioncable.connection import Connection
from actioncable.subscription import Subscription
from actioncable.message import Message
from lib.Lib_Settings import CENTRALIZER_SERVER, CHANEL_UUID


class WebSocketFuseaccess():

    def __init__(self, channel):
        url = CENTRALIZER_SERVER
        ws_url = url.replace("http", "ws", 1) + "/cable"
        self.ws_url = ws_url
        self.uuid = CHANEL_UUID
        self.channel = channel

    def create_connection(self):
        connection = Connection(url=self.ws_url)
        connection.connect()

        subscription = Subscription(connection,
                                    identifier={
                                        'channel': self.channel, 'uuid': self.uuid}
                                    )

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
