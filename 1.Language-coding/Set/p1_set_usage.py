# way1 , try to remember this

s1 = set()
s1.add(1)
s1.add(10)
s1.add(20)
deleted = s1.pop()
print(f"deleted {deleted} and s1 {s1}")

print(s1)

# iterate using loop
for i in s1:
    print(i)

# way 2
s2 = {1, 2, 3, 4, 5, 6, 1}
print(s2)
# s2.update([200]) # update takes list , no need to remember , use add instead
s2.add(300)
print(s2)

s2.remove(300)
print(f"after removing 300 {s2}")



