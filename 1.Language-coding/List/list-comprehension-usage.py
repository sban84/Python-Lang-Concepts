""" Map and list comprehension both mostly used for the same purpose
processing each item one by one in related to functional way of programming
but refer list comprehension in python in first place """

# 1.
l = [1, 2, 3, 4, 100, 200]

evens = [i for i in l if i % 2 == 0]
print(evens)

# 2.

r = [i for i in l if i > 10 if i < 150]
print(r)

# 3. Conditional List Comprehensions

l = [1, 2, 3, 4]

r = [i if i > 2 else "*" for i in l]
print(r)


# 4.

def a_complex_func(a, b):
    if a + b > 100:
        return (a + b)
    else:
        return None


l = [(50, 51), (12, 23), (60, 60)]

r = [a_complex_func(i[0], i[1]) for i in l]
print(r)

# filter operation
l = [1, 2, 3, 4, 100, 200]
r = filter(lambda x: x > 3, l)
print(f"after filter {list(r)}")
