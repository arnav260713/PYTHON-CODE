def trip_expenditure():
    print("----- Trip Expenditure Calculator -----")

    # Hotel cost
    hotel_per_day = float(input("Enter hotel cost per day: ₹"))
    days = int(input("Enter number of days stayed: "))
    total_hotel = hotel_per_day * days

    # Plane cost
    plane_cost = float(input("Enter plane ticket cost: ₹"))

    # Vehicle rental cost
    vehicle_cost = float(input("Enter vehicle rental cost: ₹"))

    # Total expenditure
    total = total_hotel + plane_cost + vehicle_cost

    print("\n----- Trip Summary -----")
    print("Hotel cost for", days, "days: ₹", total_hotel)
    print("Plane cost: ₹", plane_cost)
    print("Vehicle rental cost: ₹", vehicle_cost)
    print("Total trip expenditure: ₹", total)


# Run the program
trip_expenditure()