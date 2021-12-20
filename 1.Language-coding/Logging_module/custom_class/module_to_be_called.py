

import logging
logger = logging.getLogger(__name__)
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.DEBUG)
c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
# Add handlers to the logger
logger.addHandler(c_handler)

def add(a,b):
    logger.debug(f"Inside module_to_be_called.py {a} and {b}") # Not sure why not called, should get printed :(
    logger.warning(f"Inside module_to_be_called.py {a} and {b}")
    logger.info(f"Inside module_to_be_called.py {a} and {b}")
    logger.error(f"Inside module_to_be_called.py {a} and {b}")
    print(a+b)
    return  a+b


if __name__ == "__main__":
    add(4,4)
