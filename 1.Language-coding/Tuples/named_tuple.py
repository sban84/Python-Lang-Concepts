from typing import NamedTuple

class Car(NamedTuple):
    color : str
    mileage : float
    automatic: bool

c = Car("red", 12.1 , 10)
print(c.color)

# c.color = "Black" # AttributeError: can't set attribute as tuples are immutable

# normal tuple
tup = (1,"a", 2.3 , False)
print(tup[3])

for i in tup:
    print(i)

t = (1,2)
print(t.index(2))
