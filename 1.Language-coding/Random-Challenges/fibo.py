def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# below code is only to understand a module can act as stand alone python script
# refer the code "module_understand" for details
# if __name__ == "__main__":
#     print("Running the module as stand alone main python file ")
#     import sys
#     fib(sys.argv[0])
#     fib2(sys.argv[0])


