# 1. public

class StudentA:

    # def __int__(self, name, score, gender , age):
    #     self.name = name
    #     self.age=age
    #     self.score = score
    #     self.gender = gender

    def __init__(self, name, score, gender, age=0):
        self.name = name
        self.__gender = gender
        self.age = age
        self._score = score

    def speak(self, language):
        print(f"I speak {language}")

    def score(self):
        print(f"my score is protected access , only instance and subclass can access")
        return self._score

    def gender(self):
        print(f"my gender is private access , only this class can access")
        return self.__gender

    @property
    def score(self):
        return self._score


student = StudentA("Ram", 90, "M", 12)
print(student.name)
print(student.age)
print(student._score)
print(student.gender())



print(student.score)
#print(student.__gender) # Error , 'StudentA' object has no attribute '__gender'
