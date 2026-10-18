import random

# Predefined routes
routes = {
    1: ("Pune Station", "Shivajinagar", 5),
    2: ("Swargate", "Kothrud", 8),
    3: ("Hinjawadi", "Wakad", 10)
}

# Cab rates per kilometre
cab_rates = {
    1: ("Auto", 12),
    2: ("Sedan", 18),
    3: ("SUV", 25)
}

print("===== WELCOME TO CAB BOOKING CHATBOT =====")

# Main menu loop
while True:
    print("\n----- MAIN MENU -----")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        # Step 1: Choose cab type
        while True:
            print("\n----- CHOOSE CAB TYPE -----")
            print("1. Auto - Rs.12/km")
            print("2. Sedan - Rs.18/km")
            print("3. SUV - Rs.25/km")

            cab_choice = input("Choose cab type: ").strip()

            if cab_choice in ("1", "2", "3"):
                cab_name, rate = cab_rates[int(cab_choice)]
                break
            else:
                print("Invalid cab choice. Please try again.")

        # Step 2: Choose route
        while True:
            print("\n----- AVAILABLE ROUTES -----")

            for number, route in routes.items():
                source, destination, distance = route
                print(
                    f"{number}. {source} to {destination}"
                    f" - {distance} km"
                )

            route_choice = input("Choose route (1-3): ").strip()

            if route_choice in ("1", "2", "3"):
                source, destination, distance = routes[
                    int(route_choice)
                ]
                break
            else:
                print("Invalid route. Please choose 1, 2, or 3.")

        # Step 3: Calculate fare
        fare = distance * rate

        print("\n===== BOOKING DETAILS =====")
        print("Cab Type:", cab_name)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate per km: Rs.", rate)
        print("Total Fare: Rs.", fare)

        # Step 4: Confirm or cancel before OTP
        while True:
            print("\n1. Confirm & Share OTP")
            print("2. Cancel Ride")

            confirm_choice = input("Enter your choice: ").strip()

            if confirm_choice == "1":
                # Generate a four-digit OTP
                otp = random.randint(1000, 9999)

                print("\n===== BOOKING CONFIRMED =====")
                print("Your OTP is:", otp)
                print("Share this OTP with the driver.")
                print("Ride is now locked.")
                print("Cancellation is not allowed after OTP sharing.")
                break

            elif confirm_choice == "2":
                print("\nRide cancelled before OTP sharing.")
                break

            else:
                print("Invalid choice. Enter 1 or 2.")

        # Return to the main menu after the booking process

    elif choice == "2":
        print("\nThank you for using our Cab Booking Chatbot!")
        print("Goodbye!")
        break

    else:
        print("Invalid menu choice. Please enter 1 or 2.")