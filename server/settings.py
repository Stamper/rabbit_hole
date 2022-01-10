from pathlib import Path

from environs import Env

SERVER_FOLDER = Path(__file__).parent
OUTPUT_FOLDER = SERVER_FOLDER.parent / "output"

env = Env()

LOG_LEVEL = env.str("LOG_LEVEL", "DEBUG")
RABBITMQ_HOST = env.str("RABBITMQ_HOST", "127.0.0.1")
QUEUE_NAME = env.str("QUEUE_NAME", "rabbit_hole")
THREADS = env.int("THREADS", 2)
