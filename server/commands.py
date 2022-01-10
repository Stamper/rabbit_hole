from loggers import logger, output


def add_item(*args, **kwargs):
    item_id = kwargs["id"]
    message = kwargs["message"]
    kwargs["storage"][item_id] = message
    logger.debug(f"add_item: id={item_id}, message={message}")
    output(f"AddItem: {message}")


def remove_item(*args, **kwargs):
    item_id = kwargs["id"]
    try:
        message = kwargs["storage"].pop(item_id)
        logger.debug(f"remove_item: id={item_id}")
        output(f"RemoveItem: {message}")

    except KeyError:
        logger.error(f"Item ID={item_id} not found")


def get_item(*args, **kwargs):
    item_id = kwargs["id"]
    try:
        message = kwargs["storage"][item_id]
        logger.debug(f"get_item: id={item_id}, message={message}")
        output(f"GetItem: {message}")

    except KeyError:
        logger.error(f"Item ID={item_id} not found")


def get_all_items(*args, **kwargs):
    all_message = "\n".join([x for x in kwargs["storage"].values()])
    logger.debug("get_all_items")
    output(f"GetAllItems: \n{all_message}")


COMMANDS = {
    "AddItem": add_item,
    "RemoveItem": remove_item,
    "GetItem": get_item,
    "GetAllItems": get_all_items,
}
