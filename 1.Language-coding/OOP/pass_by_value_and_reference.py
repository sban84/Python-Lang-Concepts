"""
Pass By Value Example
"""
def foo(x):
    x += 10
    print(f"x defined in foo  = {x}")
    print(f"id(x) defined in foo  {id(x)} ")


x = 5
print(f"x defined in top level = {x}")
print(f"id(x) defined in top level {id(x)} ")
foo(x)


"""
Pass by refernce 
"""

l =  [1,2,3,4,5]

def foo(l):
    l[0] = 100

print(f" l top level value = {l}")
foo(l)
print(f" l top level value = {l}")













