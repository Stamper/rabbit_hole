import json
from functools import wraps
from typing import Any, Callable, Dict, TypeVar, cast

from pika import BlockingConnection, ConnectionParameters
from settings import QUEUE_NAME, RABBITMQ_HOST

FuncT = TypeVar("FuncT", bound=Callable[..., Any])


def rabbitmq_connection(func: FuncT) -> FuncT:
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        connection = BlockingConnection(ConnectionParameters(RABBITMQ_HOST))
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE_NAME)
        kwargs["channel"] = channel
        func(*args, **kwargs)
        channel.close()

    return cast(FuncT, wrapper)


@rabbitmq_connection
def send_message(message: Dict[str, str], *, channel: Any) -> None:
    channel.basic_publish(
        exchange="", routing_key=QUEUE_NAME, body=json.dumps(message).encode()
    )
