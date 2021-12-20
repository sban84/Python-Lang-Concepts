""" The difference between return and yield is that returns exits from the function
 and destroys all the computation and internal state and returns the o/p in one go

But in yield, it saves the state and returns one result one at a time
and returns the sec o/p upon calling next(generator) / loop internally calls the same next
as shown below"""
from time import time


def calculate_time(func):
    def wrapper_cal_time(n):
        start = time()
        result = func(n)
        # print(result)
        end = time()
        print(f"{func.__name__} took {end - start} sec")
        return result

    return wrapper_cal_time


@calculate_time
def fibo(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    result = fibo(6)
    print(",".join([str(i) for i in result]))

    result = fibo(6)
    for i in result:
        print(i, end=",")

    print("\n")
    result = fibo(6)
    print(next(result))
    print(next(result))
