
def fact(n:int):
    if (n == 1) or (n == 0):
        return 1
    else:
        return n * fact(n-1)


for i in range(1,11):
    result = fact(i)
    print(f"Factorial of {i} is {result}")

print(fact(0))
