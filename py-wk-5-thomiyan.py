# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"I am {self.name} from {self.origin}, and I wield the power of {self.power}!"

    def use_power(self):
        return f"{self.name} uses {self.power} to save the day!"

# Subclass demonstrating inheritance and encapsulation
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.__flight_speed = flight_speed  # Encapsulated attribute

    def use_power(self):
        return f"{self.name} soars through the skies at {self.__flight_speed} km/h using {self.power}!"

    def get_flight_speed(self):
        return self.__flight_speed




# Example Usage
hero1 = Superhero("Ayanda Thomas", "Fire Manipulation", "Wetlands")
hero2 = FlyingHero("Ethan", "Wind Control", "Cloud City", 800)

print(hero1.introduce())
print(hero1.use_power())

print(hero2.introduce())
print(hero2.use_power())
print(f"Flight speed: {hero2.get_flight_speed()} km/h")




# Activity 2: Polymorphism — Vehicles in Motion
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving"

class Plane(Vehicle):
    def move(self):
        return "Flying"

class Boat(Vehicle):
    def move(self):
        return "Sailing"


# Example Usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
