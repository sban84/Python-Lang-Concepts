import collections

"""Note: OrderedDict is not a built-in part of the core language and must be imported from the collections module in 
the standard library. While standard dict instances preserve the insertion order of keys in CPython 3.6 and above, 
this was simply a side effect of the CPython implementation and was not defined in the language spec until Python 
3.7. So, if key order is important for your algorithm to work, then it’s best to communicate this clearly by 
explicitly using the OrderedDict class: """
d = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(d.keys())
ordered_dict = collections.OrderedDict()
ordered_dict.update(d)
print(f"ordered_dict {ordered_dict}")

# access items same as normal dict
print(ordered_dict.get("a"))

# remove same as normal dict use pop("key")

deleted = ordered_dict.pop("b", "default_value")
print("deleted", deleted)

# iterate
print("Iterate dict")
for (k, v) in ordered_dict.items():
    print(f"key = {k} , value = {ordered_dict.get(k)}")

# 2. difference between OrderedDict and defaultdict
names_str = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith"
names_list = names_str.split(" ")

names_ordered_dict = collections.OrderedDict()
names_default_dict = collections.defaultdict(int)
for n in names_list:
    # names_ordered_dict[n] += 1 Error if the key is not present
    names_default_dict[n] += 1  # allowed as initialized to 0 based on default_factory int
    # for names_ordered_dict we need normal approach as below,
    if n not in names_ordered_dict:
        names_ordered_dict.update({n: 1})
    else:
        names_ordered_dict.update({n: names_ordered_dict.get(n) + 1})

print(f"names_default_dict {names_default_dict}")
print(f"names_ordered_dict {names_ordered_dict}")
