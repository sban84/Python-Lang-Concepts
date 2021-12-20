# 1. Consolidate 2 given lists into one and sort results
from collections import Counter

a = [1, 2, 3, 4]
b = [30, 20, 10, 40]

a.extend(b)
sorted_list = sorted(a)

print(sorted_list)

# 2. sort a list , check merge_sort.py

#  3. Find the minimum number from the list

lst = [11, 2, 3, 4]
lst.sort()
print(f"maximum item of {lst} is", lst[len(lst) - 1])

# 4. Count the number of distinct elements in an area/dictionary (and then change)
lst = [11, 2, 3, 4, 11]
counter = Counter(lst)
print(counter)

result = [k for k, v in counter.items() if v % 2 == 1]
print("No. of distinct items ", len(result))

# 5. Count the number of common characters between two strings

s1 = "hello"
s2 = "hlasao"

# way 1 using set
set1 = set(s1)
set2 = set(s2)
common = set1.intersection(set2)
print(common)

# way 2 , using string contains
result_set = set()
if len(s1) > len(s2):
    for i in s1:
        if i in s2:
            result_set.add(i)
else:
    for i in s2:
        if i in s1:
            result_set.add(i)

print("result_set", result_set)

#  6. Update keys from normal case (or snake case) to camel case

# Snake case to camel case

s = "snake_case_name"

result = ''.join([w.title() for w in s.split("_")])
print(result)

# CamelCase to snake_case

import re

name = 'CamelCaseName'
name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print(name)


import re
s = "FirstNameFull"
c = re.compile(r'(?!^)(?=[A-Z])' )
res =  re.sub(c, '_', s).lower()
print(res)
