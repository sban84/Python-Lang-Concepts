def say_hello(name):
    return f"Hello {name}"


""" Now lets say we wanted to enhance or wanted to add some more functionality without changing
the current code of say_hello()
decorators is of help """


def add_greeting(func):
    def wrapper_say_hello(name):
        result = func(name)
        return result

    return wrapper_say_hello  # Note no () here as we are returning function not executing.


# way1 , i.e some thing called higher order functions in functional programming
# function is first class citizen i.e. everything is functions
# 1. works as variables  2. passing function as arg 3. return function

func = add_greeting(say_hello)  # a function reference
print(func("SBAN"))


# way2
@add_greeting
def say_hello(name):
    return f"Hello {name}"


print(say_hello("SBAN"))


# here *a is nothing but varargs
def add_1(*a):
    sum = 0
    for i in a:
        sum += i
    return sum


def add_2(func):
    def wrapper_func(**a):
        return func(**a)

    return wrapper_func


# res1 = add_2(add_1)
# print(res1(1))
print(add_1(1, 2, 3))
