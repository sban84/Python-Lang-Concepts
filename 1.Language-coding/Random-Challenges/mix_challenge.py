from dataclasses import dataclass
from collections import namedtuple

from dateutil.relativedelta import relativedelta
from datetime import datetime


# 1 Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
def convert_date_format(date: str):
    formatted_dte = datetime.strptime(date, "%m/%d/%Y")
    print(formatted_dte)
    formatted_str = datetime.strftime(formatted_dte, "%Y%d%m")
    print(formatted_str)


convert_date_format("11/12/2019")


# 2. Create a function that takes two number strings and returns their sum as a string.

def add_num(a: str, b: str):
    try:
        if (a is None) | (b is None):
            raise ValueError("Num is None")
        if (a.isnumeric()) & (b.isnumeric()):
            result = int(a) + int(b)
            return str(result)
        else:
            raise ValueError("Num is not numeric")
    except ValueError as e:
        print(e)


print(add_num("111", "222a"))

# 3. Given string contains a combination of the lower and upper case letters.
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

s = "HelO"
lower_chars_first = "".join(sorted(s, reverse=True))
print(lower_chars_first)  # leOH


# 4. String sorting-searching is based on ASCII values of the chars

def full_sort(s):
    sorted_str = "".join(sorted(s))
    print(sorted_str)


s = full_sort("AabCDea")  # ACDaabe
print(s)


# 5. But if we wanted to sort by all lower case first then uppercase then we need to
# tweak a lit the code ,
def custom_sorting_string(s: str):
    lower_str = ""
    upper_str = ""
    for c in s:
        # print(c)
        if c.islower():
            lower_str += c
        else:
            upper_str += c

    print(lower_str)
    print(upper_str)
    final_sorted_str = "".join(sorted(lower_str) + sorted(upper_str))
    print(final_sorted_str)


custom_sorting_string("AabCDea")


# 6. Subarray with Given Sum , You are given an array of numbers (non-negative).
# Find a continuous subarray of the list which adds up to a given sum.
# arr1 = [1, 7, 4, 2, 1, 3, 11, 5,5] target1 = 10

@dataclass
class RsultSet():
    start: int
    end: int
    length: int


# main logic
def subarray_with_specific_sum(lst: list, n: int):
    resultset = []
    start_pointer = 0
    end_pointer = len(lst)

    temp_sum = 0
    temp_counter = 0
    while start_pointer < end_pointer:
        temp_sum += lst[start_pointer]
        print("temp_sum", temp_sum)
        if temp_sum < n:
            start_pointer += 1

        if temp_sum == n:
            print(f"found max subarray from {temp_counter} and {start_pointer}")
            # resultset.append((temp_counter, start_pointer, (start_pointer - temp_counter + 1)))
            resultset.append(RsultSet(temp_counter, start_pointer, (start_pointer - temp_counter + 1)))

        if temp_sum > n:
            temp_sum = lst[start_pointer]
            temp_counter = start_pointer
            start_pointer += 1

    print("RsultSet >> ", RsultSet)
    max_diff_so_far = None
    temp_max = resultset[0].length
    for i in resultset:
        print(i.length, temp_max)
        if i.length >= temp_max:
            max_diff_so_far = i
    print(max_diff_so_far)

    # max_diff = 0
    # temp_diff = 0
    # for i in resultset:
    #     diff = i[2]
    #     print(diff)
    #     if diff > temp_diff:
    #         temp_diff = i[2]
    #         max_diff = (i[0], i[1])

    # print(max_diff)


# subarray_with_sum([1, 7, 4, 2, 1, 3, 11, 5, 5], 10)
subarray_with_specific_sum([1,2,4,5,6,7], 15)


# 7. Array with Max Sum

from sys import maxsize


# Function to find the maximum contiguous subarray
# and print its starting and end index
def maxSubArraySum(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    temp_index = 0

    for i in range(0, size):

        max_ending_here += a[i]
        print(f"max_ending_here {max_ending_here}")
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = temp_index
            end = i
            print(f"max_so_far {max_so_far}")

        if max_ending_here < 0:
            max_ending_here = 0
            temp_index = i + 1

    print("Maximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))


# Driver program to test maxSubArraySum
a = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSubArraySum(a, len(a))
