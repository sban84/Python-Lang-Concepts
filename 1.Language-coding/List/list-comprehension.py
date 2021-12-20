
# 1.
import time


def even(i):
    if i % 2 == 0:
        return i
    else:
        return "*"


r = [even(i) for i in range(10)]  # [0, '*', 2, '*', 4, '*', 6, '*', 8, '*']
print(r)
r = [ i if i% 2 == 0 else "*" for i in range(10)]
print(r)


# 2.
def f(x):
    import time
    time.sleep(0.1)
    return x ** 2


start = time.time()
r = [f(i) for i in range(10) if f(i) > 10]
print(r)
print("time taken using function call called 2 times(try avoiding) ", time.time() - start)

"""" Mostly for small code logic its good to add in one line 
but for complex codes its better to add in a function use that in list comprehension"""
start = time.time()
r = [v for v in (f(i) for i in range(10)) if v > 10]
print(r)
print("time taken function call 1 times ", time.time() - start)

# 3.
start = time.time()
temp_list = [f(i) for i in range(0, 10)]

r = [i for i in temp_list if i > 10]
print(r)
print("time taken", time.time() - start)


