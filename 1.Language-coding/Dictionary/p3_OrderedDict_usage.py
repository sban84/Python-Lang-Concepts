import collections
"""Note: OrderedDict is not a built-in part of the core language and must be imported from the collections module in 
the standard library. While standard dict instances preserve the insertion order of keys in CPython 3.6 and above, 
this was simply a side effect of the CPython implementation and was not defined in the language spec until Python 
3.7. So, if key order is important for your algorithm to work, then it’s best to communicate this clearly by 
explicitly using the OrderedDict class: """
d = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

print(d.keys())
ordered_dict = collections.OrderedDict()
ordered_dict.update(d)
print(f"ordered_dict {ordered_dict}")

# access items same as normal dict
print(ordered_dict.get("a"))

# remove same as normal dict use pop("key")

deleted = ordered_dict.pop("b" , "default_value")
print("deleted" , deleted)

# iterate
print("Iterate dict")
for (k,v) in ordered_dict.items():
    print(f"key = {k} , value = {ordered_dict.get(k)}")

