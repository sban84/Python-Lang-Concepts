s1 = {1, 2, 3, 4}
s2 = set()
s2.add(4)  # one item only
s2.update([5, 6, 7, 10])  # takes iterable.

# s1.remove(10) # removes but no return , throws KeyError for non existent item
# s1.pop(10) # removes and returns , so better to remember this , throws KeyError for non existent item

s3_union = s1.union(s2)
print(s3_union)
