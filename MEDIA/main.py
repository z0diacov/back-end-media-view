import asyncio
from rabbitmq import rabbitmq_client
from rabbit_callbacks import message_calback
from security.config import RABBITMQ_QUEUES

async def main():
    try:
        print("Media started. Connecting to RabbitMQ...")
        await rabbitmq_client.connect()
        if rabbitmq_client.channel is None:
            raise RuntimeError("RabbitMQ channel is not initialized. Connection failed.")
        
        print("Connected. Waiting for messages...")

        await rabbitmq_client.add_consumer(RABBITMQ_QUEUES['from_main'], message_calback) 

        stop_event = asyncio.Event()
        await stop_event.wait()
    
    except KeyboardInterrupt:
        print("Shutting down...")
    
    except Exception as e:
        print(f"Critical error: {e}")

    finally:
        await rabbitmq_client.disconnect()
        print("Disconnected from RabbitMQ.")

if __name__ == '__main__':
    asyncio.run(main())
