# OOPs Concepts - Create a Vehicle class and inherit it in Car and Bike classes.

class Vehicle:
    def __init__(self, name, model,year):
        self.name = name
        self.model = model
        self.year = year

    def display(self):
            print(f"Vehicle Name: {self.name}, Model: {self.model},Year: {self.year}")

class Car(Vehicle):
    def display(self):
        print(f"Car Name: {self.name}, Model: {self.model}, Year: {self.year}")

class Bike(Vehicle):
    def display(self):
        print(f"Bike Name: {self.name}, Model: {self.model}, Year: {self.year}")

#creating objects
truck =Vehicle("Truck" ,"T-1000",2002)
car = Car("Toyota", "Corolla", 2020)
bike = Bike("Yamaha", "FZ", 2019)

truck.display()
car.display()
bike.display()
