class Vehicle:
    """
    A base class with a generic move() method.
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def move(self):
        """
        A generic method that will be overridden in subclasses.
        """
        print(f"The {self.make} {self.model} is moving.")

class Car(Vehicle):
    """
    A Car class that overrides the move() method.
    """
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def move(self):
        """
        Provides a specific implementation of move() for a car.
        """
        print(f"The {self.year} {self.make} {self.model} is driving... 🚗")

class Plane(Vehicle):
    """
    A Plane class that overrides the move() method.
    """
    def __init__(self, make, model, year, max_altitude):
        super().__init__(make, model, year)
        self.max_altitude = max_altitude
        
    def move(self):
        """
        Provides a specific implementation of move() for a plane.
        """
        print(f"The {self.year} {self.make} {self.model} is flying... ✈️")
        print(f"It's soaring high at {self.max_altitude} feet.")

# Main program to demonstrate polymorphism.
if __name__ == "__main__":
    # Create instances of the subclasses.
    my_car = Car("Ford", "Mustang", 1965, 2)
    my_plane = Plane("Boeing", "747", 1970, 45000)

    # Create a list containing different types of objects.
    vehicles = [my_car, my_plane]

    # Iterate through the list and call the same method on each object.
    # The output is different for each one because of polymorphism.
    print("--- Polymorphism in action! ---")
    for vehicle in vehicles:
        vehicle.move()
        print("-" * 20)