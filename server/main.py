import threading
from typing import Dict

from commands import COMMANDS
from loggers import logger
from pika import BlockingConnection, ConnectionParameters
from pika.exceptions import (
    AMQPChannelError,
    AMQPConnectionError,
    ConnectionClosedByBroker,
)
from pydantic import ValidationError
from schemas import Package, Storage
from settings import QUEUE_NAME, RABBITMQ_HOST, THREADS

storage: Dict[str, str] = Storage()
lock = threading.Lock()


def on_message_callback(ch, method, _properties, body):
    t_id = threading.get_ident()
    try:
        package = Package.parse_raw(body)
        logger.debug(f"Thread-{t_id}: {package}")

    except ValidationError:
        logger.error(f"Invalid message format: {body}")
        return

    try:
        processor = COMMANDS[package.command]
        params = dict(package)
        params["storage"] = storage
        with lock:
            processor(**params)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except KeyError:
        logger.error(f"Command is not implemented: {package.command}")


def consume() -> None:
    t_id = threading.get_ident()
    while True:
        try:
            connection = BlockingConnection(
                ConnectionParameters(RABBITMQ_HOST)
            )
            channel = connection.channel()
            channel.queue_declare(queue=QUEUE_NAME)
            channel.basic_consume(QUEUE_NAME, on_message_callback)
            logger.debug(f"Thread-{t_id}: Consuming started")
            channel.start_consuming()

        except ConnectionClosedByBroker:
            logger.error(f"Thread-{t_id}: Connection was closed by broker")
            break

        except AMQPChannelError:
            logger.error(f"Thread-{t_id}: Channel error")
            break

        except AMQPConnectionError:
            logger.debug(f"Thread-{t_id}: Recovering connection")
            continue


if __name__ == "__main__":
    for _ in range(THREADS):
        new_thread = threading.Thread(target=consume)
        new_thread.start()
