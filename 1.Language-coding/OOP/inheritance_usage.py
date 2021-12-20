class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def leg(self):
        print("Dogs has 4 legs")


class Bulldog(Dog):
    # nothing override
    pass


"""One thing to keep in mind about class inheritance is that changes to the parent class
automatically propagate to child classes. This occurs as long as the attribute or
method being changed isn’t overridden in the child class."""


class JackRussellTerrier(Dog):

    # override super class speak def
    def speak(self, sound="woof"):  # default value in arg
        return f"{self.name} says {sound}"

    # this is new def available to subclass only, no relation with super class.
    def price(self):
        return "JackRussellTerrier Price"


jack = JackRussellTerrier("JackRussellTerrier", 12)
print(jack.speak())
print(jack.price())
print(jack.leg())

bulldog = Bulldog("Bulldog", 10)
print(bulldog.speak("Hi"))
