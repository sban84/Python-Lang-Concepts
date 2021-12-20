# 1,
l = [100, 1, 2.0, 1.0, 300]
print(l)
l.reverse()  # in place reverse a list
print(l)

# 2. best way remember this
l = [100, 1, 2.0, 1.0, 300]
rev_l = reversed(l)  # returns a new list with reversed
print(list(rev_l))

# 3. by index
l = [100, 1, 2.0, 1.0, 300]
rev = l[::-1]
print("by index", rev)


# Iterative Way , no need to remember
l = [100, 1, 2.0, 1.0, 300]
for i in range(len(l)-1, -1, -1):
    print(l[i])
