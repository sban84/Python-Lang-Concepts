"""You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2 """


def swap_case(s: str):
    result = ""
    for c in s:
        if c.isupper():
            result = result + c.lower()
        elif c.islower():
            result += c.upper()
        else:
            result += c
    return result


print(swap_case("Pythonist 2"))


def print_char_type(s: str):
    for c in enumerate(s):
        #print(c[0] , type(c[1]))
        if str(c[1]).isnumeric():
            print(f"{c[1]} is a numeric")
        # chars  check
        elif str(c[1]).isascii():
            if str(c[1]).isspace():
                print(f"{c[1]} is a space")
            elif c[1] in ['/','#','*']:
                print(f"{c[1]} is a special char")
            else:
                print(f"{c[1]} is a char")


print_char_type("Hello 2#/a")




