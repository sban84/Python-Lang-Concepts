animals = [
    'bird',
    'fish',
    'elephant',
]

# usage 1 , to get the index and also the item same time
for (idx, i) in enumerate(animals):
    print(f"idx = {idx} and i {i}")

# usage 2,
for (first_char, *_, last_char) in animals:
    print(first_char, last_char)

(first_char, last_char) = "a", "b"
print(first_char, last_char)

a, b = 10, 12
print(a, b)

a, b, c = ([1, 2], 3, [10, 11])
print(a, b, c)

a, *b, c = ([1, 2], 3, 4, 5, 6, [10, 11])
print(a, b, c)
