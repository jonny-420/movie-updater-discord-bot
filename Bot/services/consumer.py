import asyncio
import aio_pika

class consumer():

    def __init__(self, exchange, routing, user, pwd, port, host, bot, channel_id):
        self.connection = None
        self.exchange = exchange
        self.routing = routing
        self.user = user
        self.pwd = pwd
        self.port = port
        self.host = host
        self.bot = bot
        self.channel_id = channel_id

    async def connect(self):
        if self.connection != None:
            return
        print("Connecting to RabbitMQ...")
        self.connection = await aio_pika.connect_robust(
            f'amqp://{self.user}:{self.pwd}@{self.host}:{self.port}/'
        )

    async def disconnect(self):
        if(self.connection == None):
            return
        await self.connection.close()

    async def consume(self):
        if(self.connection == None):
            return
        channel = await self.connection.channel()
        await channel.set_qos(prefetch_count=1)

        exchange = await channel.declare_exchange(
            self.exchange,
            aio_pika.ExchangeType.DIRECT,
            durable=True
        )

        queue = await channel.declare_queue('movies', durable=True)
        await queue.bind(exchange, routing_key=self.routing)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    if self.bot:
                        channel = self.bot.get_channel(int(self.channel_id))
                        if channel:
                            await channel.send(f"Top 3 movies coming out \n{message.body.decode()}")