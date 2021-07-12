"""Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000"."""


def revese_a_string(result):
    rev_string = ""
    for i in result[::-1]:
        rev_string += i
    print(rev_string)



def format_number(num:int):
    s = str(num)
    string = "hello"
    result = ""
    counter = 0
    for i in range(len(s) - 1, -1, -1):
        print(s[i])
        result += s[i]
        counter +=1
        if counter == 3:
            result += ","
            counter = 0
    revese_a_string(result)
    #print(result)

# reverse a string






format_number(1000000)
