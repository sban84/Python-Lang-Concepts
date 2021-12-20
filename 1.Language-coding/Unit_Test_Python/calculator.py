""" In This code explains different types of methods and their usage
But also Test cases around it"""

import traceback


class Calculator:
    # class attribute
    instance_counter = 0

    def __init__(self):
        self.number_to_add = 10

    @staticmethod
    def divide(a, b):
        """since this method is not utilizing any instance variables, better to mention as
         static methods"""
        return a / b
        # try:
        #     return a /b
        # except ValueError as e:
        #     traceback.format_exc()
        #     raise e

    def add(self, a):
        """ for example this is using instance variable number_to_add
        so need to be a instance method not static nor classmethod"""
        if a is not None:
            return a + self.number_to_add
        else:
            raise TypeError("Number need to be valid")

    @classmethod
    def get_instance_count(cls):
        cls.instance_counter += 1
        return cls.instance_counter


if __name__ == "__main__":
    c = Calculator()
    try:
        Calculator.divide(12, 0)
    except ZeroDivisionError as e:
        traceback.print_exception(type(e), e, e.__traceback__)
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)

    print(c.add(12))
    print(c.get_instance_count())
