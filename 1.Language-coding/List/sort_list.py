l = [2, 1, 10, 100, 211, 4, 4]

l.sort()
print(f"Inplace sorting {l}")

l.reverse()
print(f"after inplace revering {l}")
sorted_list = sorted(l)
print(f"returning new list sorting {sorted_list}")

# 2,
print("demo for sorting list of tuples using key ")
a_list = [(1, 2), (5, 1), (3, -1), (100, 200)]

sorted_list_default = sorted(a_list)
print(sorted_list_default) # by default its by first item in the tuple [(1, 2), (3, -1), (5, 1), (100, 200)]

sorted_list = sorted(a_list, key=lambda x: x[1], reverse=False)
print(sorted_list)  # [(3, -1), (5, 1), (1, 2), (100, 200)]

print("demo for sorting list of dict using key ")
a_list = [
    {"name": "a", "age": 10},
    {"name": "c", "age": 100},
    {"name": "b", "age": 21},
]
sorted_list_by_age_desc = sorted(a_list, key=lambda kv: kv["age"], reverse=True)
print(sorted_list_by_age_desc)  # [{'name': 'c', 'age': 100}, {'name': 'b', 'age': 21}, {'name': 'a', 'age': 10}]
