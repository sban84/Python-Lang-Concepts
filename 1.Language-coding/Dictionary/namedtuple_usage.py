"""
Personally I dnt use this , but just to know ,
as Using classes / DataClass will be good more OOP style
"""
from collections import namedtuple

Student = namedtuple("Student", "f_name, l_name, age")
t1 = Student("sban", "ban", "22")

print(t1.age)
# modify the attributes , need _replace
t1._replace(f_name="Ram")
print(t1.f_name)

result_dict = t1._asdict()
print(result_dict)




for i in t1:
    print(i)