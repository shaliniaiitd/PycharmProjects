class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.make} {self.model} is now running.")
        else:
            print(f"The {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.make} {self.model} has been stopped.")
        else:
            print(f"The {self.make} {self.model} is already stopped.")

# Usage
my_car = Car("Toyota", "Camry")
my_car.start()  # Starts the car
my_car.stop()   # Stops the car
my_car.start()  # Starts the car again
