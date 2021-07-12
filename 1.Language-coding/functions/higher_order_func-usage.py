"""
Python is a multi usage programming language.
1- procedural
2- OOP
3- Functional

Higher Order Functions give our code flexibility. By abstracting what functions are applied or returned, we gain more
control of our program's behavior.

Python provides some useful built-in Higher Order Functions, which makes working with sequences much easier. We'll first
look at lambda expressions to better utilize these built-in functions.
"""


def add_to_number(numbers: list, to_add: int):
    result_list = []
    increament = 0
    if to_add is not None:
        increament = to_add
    for i in numbers:
        result_list.append(i + increament)
    return result_list


orig_list = [1, 2, 3, 4, 5]

# this is onw way calling a function as mormal ,
print(add_to_number(orig_list, 2))


# a Higher Order function wrap another function and increases the scope
# normally higher order function returns another function
def hof(increament):
    result_list = []

    def add_func(numbers):
        for i in numbers:
            result_list.append(i + increament)
        return result_list

    return add_func


add2 = hof(2)
print(add2)
print(add2(orig_list))

# similarly we can easily ,

add10 =  hof(10)
final_result = add10(orig_list)
print(final_result)



