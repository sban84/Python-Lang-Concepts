from functools import reduce

lst = [1, 2, 3, 4, 5]


def product(l):
    temp = 1
    for i in l:
        temp *= i
    return temp


print(product(lst))

"""reduce takes a function and a sequence and iterates over that sequence. On each iteration, both the current element 
and output from the previous element are passed to 
the function. In the end, a single value is returned."""


def product(x, y):
    return x * y


r = reduce(lambda x, y: product(x, y), lst, 1)  # (function, iterable, initializer=None)
print(r)

r = reduce(lambda x, y: x * y, lst, 1)
print(r)
