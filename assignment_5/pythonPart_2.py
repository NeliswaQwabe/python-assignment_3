# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Derived classes
class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling")

# Function to demonstrate polymorphism
def travel(vehicle):
    vehicle.move()

# Create objects
my_car = Car()
my_plane = Plane()
my_bike = Bicycle()

# Polymorphic behavior
vehicles = [my_car, my_plane, my_bike]

for v in vehicles:
    travel(v)
