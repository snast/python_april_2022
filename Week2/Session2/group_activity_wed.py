# Write a Car class with a make, model, current fuel level, 
# mileage as an attribute, fuel and mileage can start at 0
# Write a method that will fill up the gas tank to 100
# Write a method to "drive" and use up some fuel and adds miles
# Write a method to get the "stats" of the car

class Car:
    def __init__(self, make, model, fuel_level=0, mileage=0):
        self.make = make
        self.model = model
        self.fuel_level = fuel_level
        self.mileage = mileage
    
    def fill_tank(self, amount):
        if self.fuel_level + amount > 100:
            if self.fuel_level == 100:
                print("Tank is already full")
            else:
                print("Filling tank but making sure not to spill gas")
                self.fuel_level = 100
        else:
            self.fuel_level += amount
        return self

    def drive(self, mileage):
        mpg = mileage * 2
        if mpg > 100:
            print("Too far")
        else:
            if self.fuel_level - mpg < 0:
                print(f"Not enough gas to drive {mileage} miles")
            else:
                self.fuel_level -= mpg
                self.mileage += mileage
        return self

    def stats(self):
        print("Car Stats")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Fuel Level: {self.fuel_level}")
        print(f"Mileage: {self.mileage}")
        return self


my_car = Car("Toyota", "Camry")
my_car.fill_tank(100).drive(20).drive(20).stats()