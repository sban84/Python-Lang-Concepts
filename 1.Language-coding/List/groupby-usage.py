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
