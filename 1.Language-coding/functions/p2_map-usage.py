"""
The map function allows us to apply a function to every element in an iterable object. For example, if we had a list of
names and wanted to append a greeting to the Strings, we can do the following:
"""

names = ["sban" , "rohit" , "shyam" , "debi"]

"""map(func, iterables) –> map object
Make an iterator that computes the function using arguments from each of the iterables. 
Stops when the shortest iterable is exhausted."""
iterator_result = map(lambda x: "Hello " + x, names)

# NOTE : # Recall, that map returns an iterator

for i in iterator_result:
    print(i , end=' ')


# 2. The same can be done by using list comprehension technique.
# mostly use comprehension for this kind of things in python
print("\n")
added_greetings = ["Hello " + i for i in names]
print(added_greetings)
