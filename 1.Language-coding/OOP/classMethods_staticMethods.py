"""THis explains the class and its various type of methods type

normal method: the current object is automatically passed as an (additional) first argument
classmethod: the class object is automatically passed as an (additional) fist argument
staticmethod: no extra arguments are automatically passed. What you passed to the function is what you get.
"""


class Car:
    vehicle_type = "Car"

    def __init__(self, name="default", color="default"):
        self.name = name
        self.color = color




    @classmethod  # can access only class attributes
    def class_methods(cls):
        print(f"vehicle_type {cls.vehicle_type}")

    @staticmethod
    def static_method():  # can not access class / instance attributes
        print("Welcome to the Shop")
        return Car()
        # return Car("d","d") # BTW always returns the same instance

    def price(self):  # can access only instance attributes such as self params

        if self.color.lower() == "red":
            print(f"My price is 100 Euro")
        else:
            print(f"My price is 60 Euro")


c = Car("BMW", "red")
print(c.static_method())
print(Car.static_method())

c.class_methods()
Car.class_methods()
