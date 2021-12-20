
"""Exercise 1: Given two lists create a third list by picking an odd-index
element from the first list and even index elements from the second. """

list_1 = [3, 6, 9, 12, 15, 18, 21]
list_2 = [4, 8, 12, 16, 20, 24, 28]

result = []

for idx, i in enumerate(list_1):
    # print(idx, i)
    if idx % 2 != 0:
        result.append(i)

for idx, i in enumerate(list_2):
    # print(idx, i)
    if idx % 2 == 0:
        result.append(i)

print(result)

# way 2 using extend and [1::2] and [0::2]

result = list_1[1::2]
result.extend(list_2[0::2])
print(result)

"""Exercise 2: Given a list, remove the element at index 4 and add it to 
the 2nd position and at the end of the list"""

list_1 = [34, 54, 67, 89, 11, 43, 94]
item_to_remove = list_1[4]
list_1.remove(item_to_remove)
print(list_1)

list_1.insert(2, item_to_remove)
list_1.append(item_to_remove)
print("finally after adding in 3th position ", list_1)

print(f"item can be removed from list by pop(index) {list_1.pop(2)} , after that {list_1}")

"""Exercise 3: Given a list slice it into 3 equal chunks and reverse each chunk"""
list_1 = [34, 54, 67, 89, 11, 43, 94]


def chunks(lst, n):
    """Yield successive n-sized chunks from the list."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


sliced_list = chunks(list_1, 3)
#
for i in sliced_list:
    print(i)

print(list(sliced_list))

# way 2 without using yield,but using comprehension
list_1 = [34, 54, 67, 89, 11, 43, 94]
n = 3
result = [list_1[i:i + n] for i in range(0, len(list_1), n)]
print(result)
reversed_list = []
for i in result:
    # print(type(i))
    reversed_list.append(list(reversed(i)))

for i in reversed_list:
    print(i)

""" zipping lists """
list_1 = ["sban", "Rohit", "Shyam"]
list_2 = ["Banerjee", "Chatterjee", "Maji"]

for i in zip(list_1, list_2):
    print(i[0], i[1])

"""
Exercise 4: Iterate a given list and count the occurrence of each element and create a dictionary 
to show the count of each element"""

from collections import Counter

list_1 = ["sban", 2, "ban", "sban", 2]
print(list_1)

counter_map = Counter(list_1)
print(counter_map)
for k, v in sorted(counter_map.items(), key=lambda kv: kv[1], reverse=False):
    print(f" key = {k} , value = {v}")

"""Exercise 5: Given a two list of equal size create a Python set such that it shows the 
element from both lists in the pair"""

list_1 = ["sban", "Rohit", "Shyam"]
list_2 = ["Banerjee", "Chatterjee", "Maji"]

result_set = set()
for i in zip(list_1, list_2):
    result_set.add(i)

# NOTE Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic
# use case is include membership testing and eliminating duplicate entries. Set objects also support mathematical
# operations like union, intersection, difference, and symmetric difference.
for i in result_set:
    print("result_set ", i)

"""Exercise 6: Given the following two sets find the intersection and remove 
those elements from the first set"""

s1 = {"a", "b", 1, 2}
s2 = {"a", "c", 1, 21}
common_items = s1.intersection(s2)
print(common_items)

for i in common_items:
    s1.remove(i)
print(f"after removing the common itmes {s1}")

"""Exercise 7: Given two sets, Checks if One Set is a subset or superset of another Set. if the 
subset is found delete all elements from that set"""

firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}

print("firstSet.issubset(secondSet)", firstSet.issubset(secondSet))  # true
print("secondSet.issubset(firstSet)", secondSet.issubset(firstSet))

print("firstSet.issuperset(secondSet)", firstSet.issuperset(secondSet))
print("secondSet.issuperset(firstSet)", secondSet.issuperset(firstSet))  # true

# secondSet.difference_update(firstSet)
# print(secondSet)
if firstSet.issubset(secondSet):
    firstSet.clear()

print(firstSet)
print(secondSet)
