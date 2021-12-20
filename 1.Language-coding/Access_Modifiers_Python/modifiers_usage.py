import logging
from logging.handlers import RotatingFileHandler

from logging.config import fileConfig


class Student:
    """
    VERY GOOD example 1. to know access modifiers in Python
    @property is used to get the value of a private attribute without using any getter methods.
    We have to put a line @property in front of the method where we return the private variable.
    To set the value of the private variable, we use @method_name.setter in front of the method.
    We have to use it as a setter.

    2. also how to use file config as log properties for configure log configurations
    3. log config has rotation log configuration which is very common in production env.

    """
    fileConfig('log_config.conf')
    logger = logging.getLogger(__name__)

    # logger.setLevel(logging.DEBUG)
    #
    # logFilePath = "my.log"
    # #formatter = "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s,datefmt = '%Y-%m-%dT%H:%M:%S'"
    # f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # file_handler = logging.handlers.RotatingFileHandler(
    #     filename=logFilePath, maxBytes=2, backupCount=10)
    # file_handler.setFormatter(f_format)
    # file_handler.setLevel(logging.DEBUG)
    # logger.addHandler(file_handler)

    def __init__(self, name, age, tuition_fee):
        if (name is None) | (name == ''):
            # self.logger.debug("name can not be Empty")
            self.logger.debug("Name Can not be Null or Empty ....")
            self.logger.error("Name Can not be Null or Empty ....")
            raise ValueError("name can not be Empty")

        self.name = name  # public
        self._age = age  # protected , general code convention is _ for protected attributes
        self.__tuition_fee = tuition_fee  # private variable or property in Python , __ for private

    def __repr__(self):
        return f"Student has name {self.name} and age {self._age} and tuition_fee {self.__tuition_fee}"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def tuition_fee(self):
        return self.__tuition_fee

    @tuition_fee.setter
    def tuition_fee(self, t):
        self.__tuition_fee = t


s1 = Student("sban", 12, 100)
s1._age = 23
print(s1)
print(f"using getter in python was {s1._age}")

"""NOTE :  Python prescribes a convention of prefixing the name of the 
variable/method with a single or double underscore to 
emulate the behavior of protected and private access specifiers.

protected -> Python doesn't have any mechanism that effectively restricts access to any 
instance variable or method.

private -> The double underscore __ prefixed to a variable makes it private. It gives a strong suggestion not to touch it 
from outside the class. 
Any attempt to do so will result in an AttributeError:
"""


# s1.__tuition_fee # Not allowed

# Inheritance
class International(Student):
    def __init__(self, name, age, tuition_fee):
        super().__init__(name, age, tuition_fee)

    def __repr__(self):
        return f"{self.__class__} has name {self.name} and age {self._age} and tuition_fee {super().tuition_fee}"
        # Note since _age is protected so accessible in subclass but __tuition_fee can not be directly accessed.
        # so we used parent class's getter API which is visible to all.


a_student = International('a', 23, 200)
print(a_student)
a_student.tuition_fee = 300
print(a_student)
