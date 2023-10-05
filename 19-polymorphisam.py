
""" Polymorphism is often used in Class methods, where we can have multiple classes with the same method name. """
# Class Polymorphism
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("drive")

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Sail")

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly")

car = Car("Ford", "Mustang");
boat = Boat("Ibiza", "Touring 20");
plane = Plane("Boeing", "747");

car.move();
boat.move();
plane.move();

