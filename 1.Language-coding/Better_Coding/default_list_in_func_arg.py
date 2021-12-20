"""passing default arg value to mutable data structure is not suggested.
instead initialize = None OR
remove the default initialization.
"""


def func(names, combined_list=[]):
    for n in names:
        combined_list.append(n)
    return combined_list


print(func(["a", "b", "c"]))
print(func(["a", "b", "c"]))  # as combined_list=[] will be initialized
# only once when the func gets loaded first time call. #o/p ['a', 'b', 'c', 'a', 'b', 'c']
