"""#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last"""


def print_full_name(first, last):
    # Write your code here
    return "Hello " + first + last + "!" + " You just delved into python."


str1 = input("Enter your first name ")
str2 = input("Enter your second name")
print(print_full_name(str1,str2) )
