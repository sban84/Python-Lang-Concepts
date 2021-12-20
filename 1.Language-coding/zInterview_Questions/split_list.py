lst = ["I am Suman and I am in Berlin"]

result = []
for i in lst:
    result.extend(i.split(" ")) # += also same here

print(result)
