import sys
import traceback



def add(a, b):
    # print(a+b)
    return a + b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Error occurred for b= {b}")
        traceback.print_exception(type(e), e, e.__traceback__)
        # traceback.format_exc(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":

    print(div(2, 0))
    print(add(2, 3))
    print(sys.path)
