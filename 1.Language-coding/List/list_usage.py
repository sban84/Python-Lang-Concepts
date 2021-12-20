# print the index of collection DS

l = [1,2,3]
print(l.index(2))
l.pop(0) # remove based on the index
for i in l:
    print(f"index of {i} in {l} is {l.index(i)}")

# iterate using enumerate , can be used for any iterable collections
print("<----iterate using enumerate--->")
l  = [10,1,12,13,14]
for idx,i in enumerate(l):
    print(f"item {i} is at index {idx}")



