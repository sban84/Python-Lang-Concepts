
import functools
from person import Person

def comparator_func(x , y):
    if x.name == y.name:
        return x.age - y.age
    else:
        return x.name - y.name

def sortPerson(p_list: list[Person]):
    sorted_list_asc = sorted(p_list,key=lambda x : x.name , reverse=False ) # by name only
    sorted_list_desc = sorted(p_list, key= lambda x: (x.name,x.age), reverse=True) # by name
    # and age if name is same then by age
    return (sorted_list_asc,sorted_list_desc)



if __name__ == "__main__":
    employees = [
        Person("Sban" , 22),
        Person("Sban", 21),
        Person("Ram", 23),
        Person("Rohit", 25),
        Person("Akul", 25),
        Person("Zyan", 26),
    ]

    (sorted_list_asc,sorted_list_desc) = sortPerson(employees)
    print(f" after sorting employees list asc {sorted_list_asc}")
    print(f" after sorting employees list desc {sorted_list_desc}")

