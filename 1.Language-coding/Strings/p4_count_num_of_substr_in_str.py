"""In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.
Sample Input

ABCDCDC
CDC
Sample Output 2 """

def count_substring(string, sub_string):
    index_sub_str = 0
    counter = 0
    # helloel , el

    temp = ""
    for s in string:
        print(f"{s} and {sub_string[index_sub_str]}")
        print("temp" , temp)
        if (index_sub_str < len(sub_string)) & (s == sub_string[index_sub_str]):

            index_sub_str += 1
            temp += s
        else:
            index_sub_str = 0
            print("inside else")
        if temp == sub_string:
            print("found")
            counter +=1
            temp = ""
            index_sub_str = 0

    return counter


# input_str = input("Enter a string")
# sub_str = input("Enter the sub str wanted to count")
input_str = "ABCDCDC"
sub_str = "CDC"
count = count_substring(input_str , sub_str)
print(count)