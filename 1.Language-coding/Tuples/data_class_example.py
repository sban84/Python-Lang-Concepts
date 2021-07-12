import dataclasses
from dataclasses import dataclass


@dataclass
class Car:
    name: str
    mileage: float
    automatic: bool


bmw = Car("Red", 10.0, True)
honda = Car("Red", False, True) # types are not checked

print(bmw.mileage)
print(honda.mileage)
print(type(honda.mileage))
print(type(bmw.mileage))