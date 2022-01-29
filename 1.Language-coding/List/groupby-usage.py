from itertools import groupby
from collections import Counter

l = ["1", "100", "200", "1", "300", "4", "400"]

c = Counter(l)
print(c)

s = "hello python its a good python"
lst = s.split(" ")
c.update(lst)
sorted(c.items(), key=lambda kv: kv[1], reverse=True)
print(c)

# 3.
a_list = [("a", 1),
          ("b", 2),
          ("a", 3)]
dict_person = dict(a_list)
print(dict_person)

# 4.
print("groupby using itertool")
from itertools import groupby

persons = [{"name": "a", "age": 1},
           {"name": "b", "age": 1},
           {"name": "c", "age": 2}]
groupby_test = groupby(persons, key=lambda x: x['age'])  # .get('age') also same
print(type(groupby_test))

for k, v in groupby_test:
    print(f" k={k} and v={list(v)}")

