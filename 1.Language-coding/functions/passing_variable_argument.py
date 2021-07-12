# 1. Variable argument , positional based:
def func(*args):
    """

    :param a: pass any number of items
    :return: sum of them
    """
    return sum(args)


result = func(2, 3)
print(result)

result = func(2.0, 3, 10)
print(result)

l = [1, 2, 3, 4]
print(sum(l))


# 2. Variable argument , keyword based:

def func(**kwargs):
    for k, v in kwargs.items():
        print(f"k = {k} and v= {v}")


func(**{"a": 1, "b": 2})  # remember one , this ** at the begining is must
# func(a=1,b=2)
