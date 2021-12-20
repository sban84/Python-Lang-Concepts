from sys import intern

# 1. reference and value check
a = 10  # a label pointing to value and it has a memory address
print(id(a))  # printing memory address
print("a=", a)  # value

b = a  # now b also points to same memory address and both has value 10

print(id(b))  # printing memory address
print("b=", b)  # value

print(f" a b reference check {a is b}")
print(f" a b value check {a == b}")

print("\n ****** after b re-initialized **** ")

b = 20  # now b re-initialized to some diff value and memory address

print(id(b))  # printing memory address
print("b=", b)  # value

print(id(a))  # printing memory address
print("a=", a)  # value

print(f" a b reference check {a is b}")
print(f" a b value check {a == b}")

# 2. instance type check

print(isinstance(a, int))
print(isinstance("hello", str))
print(isinstance([1, 2, 3], list))
print(isinstance(12.0, int))
print(isinstance(12.0, float))

# TODO 3.intern in python, similar concept in Java.


# 4.  For Primitives values, python optimizing memory locations for same values,
# same as Strings , this concept is called String pool / primitives pool
print("\nSpecial primitives values")
a = 10
b = 10

print(a is b)

a = 257
b = 257

print(a is b)
print(id(a), id(b))

s1 = "hello"
s2 = "hello"

print(s1 is s2)
print(id(s1), id(s2))
print(id(s1) == id(s2))

