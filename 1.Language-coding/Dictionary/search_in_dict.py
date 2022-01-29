def dict_search(lod, **kw):
    return filter(lambda i: all((i[k] == v for (k, v) in kw.items())), lod)


lod = [{'a': 33, 'b': 'test2', 'c': 'a.ing333'},
       {'a': 22, 'b': 'ihaha', 'c': 'fbgval'},
       {'a': 33, 'b': 'TEst1', 'c': 's.ing123'},
       {'a': 22, 'b': 'ihaha', 'c': 'dfdvbfjkv'}]

print(list(dict_search(lod, a=22)))

# way 2 , directly , using list comprehension remember this ONLY
result = [i for i in lod if i['a'] == 22]
print(result)

# for search in dict in python is more easy using pandas,
# refer more example my pandas illustration.
import pandas as pd

df = pd.DataFrame(lod)
print(df)
print(df['a'])

# does not much makes to use filter for plain dict , as we can do same by get index access
d = {'a': 33, 'b': 12, 'c': 23}

result = filter(lambda x: x[0] == 'a', d.items())
print(dict(result))
print(d.get('a'))


# use dict comprehension
result = {k: v for k, v in d.items() if k == 'a'}
print(result)
