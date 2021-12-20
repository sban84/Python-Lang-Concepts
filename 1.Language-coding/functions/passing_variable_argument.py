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


func(**{"a": 1, "b": 2})  # remember one , this ** at the beginning is must


# func(a=1,b=2)


# 3. More complex example

# NOTE : kwarg1 is just a name , following convention that it takes kv pair
# we can pass anything, only *  and ** means variable arguments like kwargs=1
# * means positional arguments
# ** means keywords arguments
# that's it.
def func(arg1, arg2=10, *args, kwarg1, kwarg2=2, **kwargs, ):
    print(f"arg1 {arg1}"
          f"arg2 {arg2}, *args {args}, kwarg1 {kwarg1} , kwarg2= {kwarg2}"
          f"kwargs= {kwargs}")


func(1, 2, kwarg1={"a": 10})  # OKAY , as variable args are optional

func(1, 2, 3, 4, 5, kwarg1={"a": 10, "b": 300}, **{"b": 200})  # valid
func(1, 2, 3, 4, 5, kwarg1=2, kwargs=1)  # valid

#func(1, 2, 3, 4, 5,  **{"b": 200}) # invalid as required keyword-only argument: 'kwarg1'
