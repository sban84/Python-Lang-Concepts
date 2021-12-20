""""
When you use the assignment operator (=) to make one variable equal to the other, you make these variables point to the
same object in memory. This may lead to unexpected behavior for mutable objects:"""


a = [1, 2, 3]
b = a
print(a)


[1, 2, 3]
print(b)
[1, 2, 3]

a.append(4)
print(a)
[1, 2, 3, 4]
print(b)
[1, 2, 3, 4]

print(id(a))

print(id(b))


#2. diff refencnce 

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)


# 3. clone , will point diff rerence in memory address

a = [1, 2, 3]
b = a.copy()

print(a == b)

print(a is b)



