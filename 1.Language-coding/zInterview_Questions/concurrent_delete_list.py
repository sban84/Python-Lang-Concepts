import sys

"""
Points to remember here is that while popin from list list size gets changed 
and in some point list.pop(idx) may throw error  .
Never modify the list while iterating by INDEX .

But in scenarios where we know the values to be removed from the list 
then we can remove it in the loop but take a copy of the list and iterate the copy in loop
list_index_problems_1.py. 
"""
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]


idx_to_delete = [1,2,5,6]

for i in idx_to_delete:
    #print(rollNumber)
    rollNumber[i] = sys.maxsize


rollNumber = [ i for i in rollNumber if i != sys.maxsize]
print(f"after delete {rollNumber}")


# 2,
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
items_to_delete = [47,76,97]

for i in items_to_delete:
    rollNumber.remove(i)

print(f"after delete {rollNumber}")