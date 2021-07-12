"""A function that does at least one of the following is a Higher Order Function.
0- Function can be assigned to variables
1- Takes one or more functions as arguments
2- Returns a function as its result
Let's assume I have a function F1. By default, F1 is a first-class function. So I should be able to pass F1 to another function. Now, let's assume I have another function F2. If we design F2 in a way that it can take F1 as an argument, the F2 is a higher order function. That is what the definition says.
Now, let's look at a working example for both types of Higher Order Functions."""


def double(x):
    return x * 2
# 0. Function can be assigned to variables
d =  double
print(d(12))

def square(x):
    return x ** 2


def tripple(x):
    return x * 3

# 1.
# Passing Function as an argument to other function
# Functions are like objects in Python, therefore, they can be passed as argument to other
# functions. Consider the below
# example, where we have created a function greet which takes a function as an argument.

def applyF(func, x):
    return func(x)


result = applyF(square, 2)
print(result)
result = applyF(tripple, 2)
print(result)

# 2.

# Returning function
# As functions are objects, we can also return a function from another function. In the below example, the create_adder function returns adder function.
#

def applyF(x):
    def minus_y(y):
        return x - y
    return minus_y

min_12 = applyF(12)
print(min_12)

print(min_12(10))




