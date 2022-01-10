from environs import Env

env = Env()
env.read_env()

RABBITMQ_HOST = env.str("RABBITMQ_HOST", "127.0.0.1")
QUEUE_NAME = env.str("QUEUE_NAME", "rabbit_hole")
