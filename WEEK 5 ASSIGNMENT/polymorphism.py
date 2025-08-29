class Vehicle:
    def move(self):
        pass  # placeholder for child classes

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Plane(Vehicle):
    def move(self):\
        print("Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water")

# Demonstration of polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()   # Each class defines move() differently
