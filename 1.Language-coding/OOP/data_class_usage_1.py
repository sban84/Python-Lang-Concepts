"""
This module provides a decorator and functions for automatically adding generated special methods
such as __init__() and __repr__() to user-defined classes.

Data classes are one of the new features of Python 3.7. With data classes, you do not have to write boilerplate code to
get proper initialization, representation, and comparisons for your objects.
"""
from dataclasses import dataclass
from typing import List

@dataclass
class Subject:
    name: str
    score: float

@dataclass
class Student:
    name: str
    subjects: List[Subject]


subs = [ Subject("Maths",10) , Subject("Physics", 10), Subject("history" , 6)]
student_1 =  Student("sban" , subs)
print(student_1)


print(student_1.subjects)
for i in  student_1.subjects: # provides name suggestions which is good
    print(i.name) # provides name suggestions which is good

print("Printing student_1.subjects sorted by their score from ascending order")
for i in sorted(student_1.subjects , key=lambda x: x.score, reverse=False):
    print(i.name)
