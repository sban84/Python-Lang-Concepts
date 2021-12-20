""" This example demonstrates logging module usage in python"""
import logging


class Employee:
    # dummy map just to show a real use case of logging functionality
    dept_sal_map = {
        "IT": 500,
        "SALES": 1000
    }
    # This helps to provide proper names, when called directly or from another module.
    logger = logging.getLogger(__name__)
    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('file.log')
    c_handler.setLevel(logging.DEBUG)  # Debug and higher like warning , error and exceptions
    f_handler.setLevel(logging.ERROR)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def format_name(self, name: str):
        self.logger.warning(f"inside format_name with name {name}")
        return self.name.title()

    def get_sal(self, dept):
        print("Inside get_sal")
        try:
            return self.dept_sal_map[dept]
        except Exception as e:
            self.logger.exception(e)




# employee = Employee("Ram","SALES")
# employee.format_name("sban Tendulkar")
# employee.get_sal("IT")
# employee.get_sal("HR")