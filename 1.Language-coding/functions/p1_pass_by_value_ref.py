"""
the core concept is same as Java.
when we re-assign inside function , the connection is lost.
and the underlying the memory will point to diff location.
"""

def func(x):
    x = 10 # its a new value and new address. limited to this function only

    print("Inside func " , x , "and its id " , id(x))
    return x

x = 5
print(id(x))
print(func(x))
print(x)

print(id(x))
