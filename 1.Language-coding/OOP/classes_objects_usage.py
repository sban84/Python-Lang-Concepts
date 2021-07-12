class Car():
    """Car class"""
    class_attribute = "Common to all instances"
    def __init__(self , color ,mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} has {self.mileage} miles"


blue_car =  Car("Blue" , 20000)
red_car =  Car("Red" , 50000)
print(Car.class_attribute)
print(blue_car.class_attribute)

print(blue_car)
print(red_car)