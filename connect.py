import pika

class Get():
    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

