class Person():
    def __init__(self,name,age):
        self.__name = name
        self.__age =age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self,new_name):
        if isinstance(new_name,str):
            self.__name = new_name
        else:
            raise ValueError("name need to be a valid string")

    @age.setter
    def age(self,new_age):
        self.__age = new_age


    def __repr__(self):
        return f"Person = {self.name} and {self.age}"


    def __eq__(self, other):
        #print("Inside __eq__ of Person class" , self)
        if other != None:
            if isinstance(other , Person):
                return (self.name == other.name) & (self.age == other.age)
            else:
                return False
        else:
            return False


    def __hash__(self):
        #print('The hash is:' , hash((self.name, self.age)))
        return hash((self.name, self.age))