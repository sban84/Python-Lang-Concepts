from collections import defaultdict

# source = {"a": 1, "b": 1, "c": 2, "a": 10}

source = [("a", 1), ("b", 1), ("c", 2), ("a", 10)]

default_dict = defaultdict(int)
print(default_dict["a"])
normal_dict = {}
# print(normal_dict["a"]) # KeyError

for i in source:
    print(i[0], i[1])
    # default_dict.update({default_dict.get(i[0]), default_dict.get(i[0]) + i[1]}) # don't know hwy its did not work??
    default_dict[i[0]] += i[1]
    normal_dict.update({i[0]: normal_dict.get(i[0],0) + i[1]})

print(f"default_dict {default_dict}")
print(f"normal_dict {normal_dict}")
