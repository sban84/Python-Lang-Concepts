"""
The collections.ChainMap data structure groups multiple dictionaries into a single mapping.
Lookups search the underlying mappings one by one until a key is found. Insertions, updates,
AND DELETIONS ONLY AFFECT THE FIRST MAPPING ADDED TO THE CHAIN:
"""

from collections import ChainMap

dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "one": 4}
dict3 = {"inner" : {"sban" : [10,11]}}
chain = ChainMap(dict1, dict2, dict3)

print(chain) # ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4}, {'inner': {'sban': [10, 11]}})

# access , can access to only one level not nested
nested_key = chain.get("inner")
print(nested_key)
# for nested use this below one at a time
print(nested_key.get("sban"))


# add any item

chain.update({"a" : 100,"b":200})

dict4 = {"five" : 5}
chain.update(dict4)


#  update with existed key will update the fist key found
chain.update({"one" : 1000})
print(chain)

chain.update({"three" : 2000})
print(chain)
print(chain.get("three", None)) # the first matching key value will be returned.




