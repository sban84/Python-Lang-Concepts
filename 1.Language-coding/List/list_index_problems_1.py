"""Exercise 8: Iterate a given list and Check if a given element already exists in a dictionary
as a key’s value if not delete it from the list
refer concurrent_delete_list.py
"""

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
temp = rollNumber.copy()
sampleDict ={'Jhon': 47, 'Emma':69, 'Kelly':76, 'Jason':97}

# 1.
result = []
for i in rollNumber:
    if i in sampleDict.values():
        result.append(i)

print(f"Found rollNumbers {result}")



# 2. Not to modify the DS while looping as it may cause unpredicted results .
for i in temp:
    print("i= ",i)
    if i not in sampleDict.values():
        rollNumber.remove(i)


print(f"after deleting {rollNumber}")
print(temp)


"""Exercise 9: Given a dictionary get all values from the dictionary and 
add them to a list but don’t add duplicates"""

speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
result_set = set()
for k,v in speed.items():
    result_set.add(v)

print(result_set)
print(list(result_set))

"""Exercise 10: Remove duplicate from a list and create a tuple and find the 
minimum and maximum number"""


sampleList = [87, 45, 41, 65, 94, 41, 99, 94]

result_set = set(sampleList)
print(f"list = {list(result_set)}")

tup = (list(result_set))


print(f"tup= {tup}")

print(f"min = {min(tup)}")
print(f"max = {max(result_set)}") # pass any iterable in min/max.











