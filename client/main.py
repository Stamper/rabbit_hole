import secrets

import click
from pika.exceptions import AMQPConnectionError
from utils import send_message


@click.command()
@click.option("-m", "--message", help="Message to save")
@click.option("-i", "--id", "_id", help="ID of the message to get or remove")
@click.argument("command")
def process_command(message: str, _id: str, command: str) -> None:
    package = {"command": command}

    if not _id:
        _id = secrets.token_hex(4)
    package["id"] = _id

    if message:
        package["message"] = message

    try:
        send_message(package)  # type: ignore
    except AMQPConnectionError:
        print("Connection error")
        return

    print(_id)


if __name__ == "__main__":
    process_command()
