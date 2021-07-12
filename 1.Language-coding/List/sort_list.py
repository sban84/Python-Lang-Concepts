
l = [2,1,10,100,211,4,4]

l.sort()
print(f"Inplace sorting {l}")

l.reverse()
print(f"after inplace revering {l}")
sorted_list = sorted(l)
print(f"returning new list sorting {sorted_list}")