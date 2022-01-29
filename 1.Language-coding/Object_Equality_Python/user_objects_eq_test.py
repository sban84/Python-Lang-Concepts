"""
This is a very good example to understand how to impl __eq__ and __hash__()
for user custom objects in Python..Very important code .



"""


from person import Person

def test_object_quality():
    p1 = Person("sban",22)
    p2 = Person("sban", 22)

    p3 = Person("Ram" , 22)
    p4 = Person("sban" , 23)

    print(f"p1 and p2 equality check {p1 == p2}")
    print(f"p1 and p2 reference check {p1 is p2}")

    print(f"p1 and p3 equality check {p1 == p3}")
    print(f"p1 and p4 reference check {p1 is p4}")


def test_object_quality_with_hash():
    p1 = Person("sban", 22)
    p2 = Person("sban", 22)
    d = {p1:1}  # TypeError: unhashable type: 'Person' if Person class ( i.e. user objects if dont impl __hash__() )
    print(d.get(p1))




if __name__ == "__main__":
    print("Inside __main__ ")
    test_object_quality()
    test_object_quality_with_hash()







