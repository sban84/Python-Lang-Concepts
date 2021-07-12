from collections import Counter
"""
Normally its used when we wanted to keep the inventory management, 
basically item and its sum of no. of occurrences, 
so in case of one dimensional DS like list it helps to get words/item count also .
"""
counter = Counter()
counter.update({"a":10,"b":20})
print(counter)
dict = {"a" : 30 , "d" : 40 , "b" : 50}
counter.update(dict)
print(counter)
print(counter.most_common())
print(len(counter)) # counts the number of keys basically
print(sum(counter.values()) ) # sum of  values


line = "Hello World of python python is a good language in data world"
#l = [1,2,1,3,4,2]
counter = Counter()
l = line.split(" ")
same_case_list = [ i.lower() for i in l ] # just converting in lower case all items of the list, list Comprehension.

counter.update(same_case_list)
print(counter)


