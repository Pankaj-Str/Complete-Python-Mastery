class Car:
    # Constructor
    def __init__(self, model):
        """This is the constructor - it runs when we create a new car"""
        print(f"Creating a new car: {model}")
        self.model = model
        self.is_running = False
    
    # Simple method to start the car
    def start(self):
        """Method to start the car"""
        self.is_running = True
        print(f"{self.model} has started!")
    
    # Simple method to stop the car
    def stop(self):
        """Method to stop the car"""
        self.is_running = False
        print(f"{self.model} has stopped!")
    
    # Destructor
    def __del__(self):
        """This is the destructor - it runs when the car object is destroyed"""
        print(f"Goodbye {self.model}!")

# Example usage:
print("Creating a new car...")
my_car = Car("Toyota")

# Start the car
my_car.start()

# Stop the car
my_car.stop()

print("\nProgram ending...")