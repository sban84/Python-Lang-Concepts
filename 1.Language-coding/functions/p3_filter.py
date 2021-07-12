"""Filter
The filter function tests every element in an iterable object with a function that returns either True or False, only
keeping those which evaluates to True. If we had a list of numbers and wanted to keep those that are divisible by 5 we
can do the following:"""

numbers = range(0, 11)

even_numbers = filter(lambda x: x % 2 == 0, numbers)
for i in even_numbers:
    print(f"even_numbers {i}")

names = ["sban", "rohit", "shyam", "debi", "anandkumar"]
long_nmaes = filter(lambda x: len(x) > 5, names)

for i in long_nmaes:
    print(f"long_nmaes {i}")


# 2. same can be achieved by list comprehension.

def even(n):
    return n % 2 == 0


even = [i for i in numbers if even(i)]
print(even)


# 3. some times we need to write a custom function like when  multi statement logic
# code we need to write inside map / filter or any any higher order function,
def even(n):
    return n % 2 ==0

numbers = range(0, 11)
res_even = filter(lambda x : even(x) , numbers)
for i in res_even:
    print(i)


def sum(a, b):
    return a + b

# list 1
lst1 = [2, 4, 6, 8]

# list 2
lst2 = [1, 3, 5, 7, 9]

result = list(map(sum, lst1, lst2))
print(result)
