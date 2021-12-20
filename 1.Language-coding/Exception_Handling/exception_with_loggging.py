# 4. Exception Handling and logging better way to capture the errors.
# Java : IO exception are checked / compile time exception
# All Runtime exceptions are unchecked exceptions

import logging


def exception_handling(a, b):
    try:
        return a / b
    except Exception as e:
        # print(f"An exception occurred with {e}")
        logging.exception("An exception occurred")

    finally:
        print("Will execute all the time ")


exception_handling(2, 0)
