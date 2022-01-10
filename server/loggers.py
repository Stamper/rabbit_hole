import logging

from settings import LOG_LEVEL, OUTPUT_FOLDER

logger = logging.getLogger("server")
logger.setLevel(LOG_LEVEL)
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
formatter = logging.Formatter("%(levelname)s: %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

output_logger = logging.getLogger("output")
output_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(OUTPUT_FOLDER / "results.log")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s: %(message)s", "%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
output_logger.addHandler(file_handler)

output = output_logger.info
