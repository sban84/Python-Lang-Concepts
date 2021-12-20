"""
the core concept is same as Java.
when we re-assign inside function , the connection is lost.
and the underlying the memory will point to diff location.
"""


# 1. Though everything in python is objects
# But for primitives its pass by value
def func(x):
    print("Inside func before modify", x, "and its id ", id(x))
    x = 10 # its a new value and new address. x is labeled to new value

    print("Inside func after modify", x, "and its id ", id(x))
    return x


x = 5
print(id(x))
print("function call>> ",func(x))
print(x)

print(id(x))

# 2. For objects its pass by reference
l1 = [1, 2, 3]
l2 = l1
print(f"identity check {l1 is l2}")
print(f"equality check {l1 == l2}")

l3 = [1, 2, 3]
print(f"identity check {l1 is l3}")
print(f"equality check {l1 == l3}")


def func(l):
    l[0] = 100
    return l


result = func(l1)

print(f"l1 before calling func {l1}")

print(f"l1 after calling func {l1}")

print(f"result after calling func {result}")

# 3. For String object , since string is immutable so modifying it will create a new one


s = "hello"


def func(s):
    print("Before modify String  " ,id(s))
    s = "hello_new" # this s is diff than passed s
    print(id(s))


print(f"s after calling func {s}")
func(s)
print(f"s after calling func {s}")
