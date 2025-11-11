class BMW:
    def fuel_type(self):
        return "Petrol"
    
    def max_speed(self):
        return "240 km/h"


class Ferrari:
    def fuel_type(self):
        return "Petrol"
    
    def max_speed(self):
        return "340 km/h"


# Polymorphism demonstration
def car_details(car):
    print(f"Car: {car.__class__.__name__}")
    print(f"Fuel Type: {car.fuel_type()}")
    print(f"Max Speed: {car.max_speed()}")
    print("-" * 30)


# Create objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Display details using polymorphism
for car in (bmw_car, ferrari_car):
    car_details(car)