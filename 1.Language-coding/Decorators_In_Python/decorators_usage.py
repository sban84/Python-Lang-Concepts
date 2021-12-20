"""
also check fibonacci_using_yield.py
"""


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


# @ with function A name implies that we will pass the below function B as an argument to A.
# which will add some extra features on B.
# e.g. A= my_decorator , B = say_whee here...
@my_decorator
def say_whee():
    print("Whee!")


say_whee()


# without using decorator the same thing will be like this.
def say_whee_1():
    print("Whee_1!")


f = my_decorator(say_whee_1)
f()
