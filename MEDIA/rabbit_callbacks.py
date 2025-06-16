import aio_pika
import json

async def message_calback(message: aio_pika.IncomingMessage):
    async with message.process():
        body = message.body.decode('utf-8')
        data = json.loads(body)

    print(data)