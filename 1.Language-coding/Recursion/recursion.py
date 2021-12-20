# 1.add 1 to 10 numbers using recursion
from functools import reduce


def add(n):
    if n == 0:
        return 0
    else:
        # total += n
        return n + add(n - 1)


print(add(10))

# result = 0
# for i in range(0,5):
#     result += i
#
# print((f"result = {result}"))


def add_1(n, result):
    if n == 0:
        return result
    else:
        result += n
        return add_1(n - 1, result)


print(add_1(10, 0))


# 2.

def fact(n):
    # print(n)
    if (n == 1) | (n == 0):  # NOTE :- MUST , remember the parenthesis is must for more than one conditional logic
        # if n <=1: # same
        return 1
    else:
        return n * fact(n - 1)


print(f"Factorial result {fact(5)}")


# 3.
def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
        # fibo(n - 1)


print("Fibonacci Series ")
fibo(6)

# 4. add 1 to 10 numbers using reduce
print("\n")
l = range(0, 11)
r = reduce(lambda x, y: x + y, l)
print(r)

# 5. reverse a string

s = "hello"


def rev_string_normal(s):
    rev_string = ""
    for i in range(len(s) - 1, -1, -1):  # range(start,end,step) end is exclusive
        rev_string += s[i]
    return rev_string


print(rev_string_normal(s))


def rev_string_recursive(s, rev_string, i):
    if i < 0:
        return rev_string
    else:
        rev_string += s[i]
        return rev_string_recursive(s, rev_string, i - 1)


rev_string = rev_string_recursive(s, "", len(s) - 1)
print(f"reverse string using recursion {rev_string}")

# def rev_string_recursive(s , rev_string,i):
#     if i<0:
#         return ""
#     else:
#         rev_string + rev_string_recursive(s,rev_string,i -1)
#
# print(f"reverse string using recursion {rev_string}")
