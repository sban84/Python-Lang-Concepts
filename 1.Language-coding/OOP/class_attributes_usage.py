class Person:
    """A simple class."""
    species = "Homo Sapiens"
    instance_counter = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_counter += 1

    def __init__(self, name):
        self.name = name
        self.increment_instance_count()

#  This method requires neither the self nor the cls reference because
    #  they are not dependent on any instance or class attribute.
    @staticmethod
    def static_met():
        return "hello caller from static method"



instance_list = []
for i in range(0, 5):
    instance_list.append(Person(name=i))

# for p in instance_list:
#     print(p.instance_counter)

print(f"finally no of instances created {Person.instance_counter}")
print(len(instance_list))

print(Person.instance_counter)
