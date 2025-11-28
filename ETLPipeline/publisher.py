import pika

class publisher():

    def __init__(self, exchange, routing, user, pwd, port, host):
        self.connection = None
        self.exchange = exchange
        self.routing = routing
        self.user = user
        self.pwd = pwd
        self.port = port
        self.host = host

    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(f'amqp://{self.user}:{self.pwd}@{self.host}:{self.port}/')
        )
    
    def disconnect(self):
        if(self.connection == None):
            return
        self.connection.close()

    def publish(self, movie_query):
        if(self.connection == None):
            return
        channel = self.connection.channel()
        
        
        movie_query.sort(key=lambda x: x.popularity, reverse=True)
        movies_string = "\n".join([f"🎬 {m.title} - summary: {m.overview}" for m in movie_query[:3]])

        channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing,
            body=movies_string.encode()
        )
