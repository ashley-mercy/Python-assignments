class Vehicle:
    """
    A base class to represent a generic vehicle with attributes like make, model, and year.
    """
    def __init__(self, make, model, year):
        # The constructor initializes the object with unique values.
        self.make = make
        self.model = model
        self.year = year
        self.is_moving = False
        print(f"A new {self.make} {self.model} has been created.")

    def start_engine(self):
        """
        A method to start the vehicle's engine.
        """
        print(f"The engine of the {self.make} {self.model} is now running.")

    def stop_engine(self):
        """
        A method to stop the vehicle's engine.
        """
        print(f"The engine of the {self.make} {self.model} has been shut off.")

# The Car class inherits from Vehicle.
class Car(Vehicle):
    """
    A specific type of Vehicle, representing a car.
    It inherits all attributes and methods from the Vehicle class.
    """
    def __init__(self, make, model, year, num_doors):
        # Use super() to call the parent class's constructor.
        super().__init__(make, model, year)
        # Add a new, specific attribute for a car.
        self.num_doors = num_doors
    
    def drive(self):
        """
        A method specific to the Car class.
        """
        print(f"The {self.year} {self.make} {self.model} is driving with its {self.num_doors} doors.")

# The Plane class also inherits from Vehicle.
class Plane(Vehicle):
    """
    A specific type of Vehicle, representing a plane.
    It inherits all attributes and methods from the Vehicle class.
    """
    def __init__(self, make, model, year, max_altitude):
        # Call the parent class's constructor.
        super().__init__(make, model, year)
        # Add a new, specific attribute for a plane.
        self.max_altitude = max_altitude

    def takeoff(self):
        """
        A method specific to the Plane class.
        """
        print(f"The {self.year} {self.make} {self.model} is taking off, headed for an altitude of {self.max_altitude} feet.")

# Main program to demonstrate creating and using the classes.
if __name__ == "__main__":
    # Create an instance of the Car class.
    my_car = Car("Honda", "Civic", 2022, 4)
    my_car.start_engine()
    my_car.drive()
    print("-" * 20)

    # Create an instance of the Plane class.
    my_plane = Plane("Airbus", "A380", 2005, 43000)
    my_plane.start_engine()
    my_plane.takeoff()
