class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        # Get the base fare from Vehicle class
        base_fare = super().fare()
        # Add 10% maintenance charge
        total_fare = base_fare + (0.10 * base_fare)
        return total_fare


# Create Bus object with seating capacity of 50
bus = Bus(50)

print("Total Bus fare is: INR", bus.fare())