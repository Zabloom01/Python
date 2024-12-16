# Function to calculate shipping cost
def calculate_shipping(weight, price_per_pound, flat_charge):
    """Function to calculate shipping cost based on weight, price per pound, and flat charge."""
    return (weight * price_per_pound) + flat_charge

# Start of program
print("Welcome to the shipping calculator!")

# Loop to get valid weight from user
while True:
    try:
        weight = float(input("Enter weight of package that you want to ship: "))
        if weight >= 0:
            confirmation = input(f"Your package weighs {weight} lbs, is that right? (yes/no): ").lower()
            if confirmation == "yes":
                break  # Exit the loop if the weight is correct
            elif confirmation == "no":
                print("Please re-enter the weight.")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            print("Weight must be a non-negative number.")
    except ValueError:
        print("Invalid input. Please enter a valid number for weight.")

# Loop to get valid shipping type from user
while True:
    shipping_type = input("Enter your shipping preference:\n 1. Ground\n 2. Drone\n ").strip().lower()
    if shipping_type == "1" or shipping_type == "ground":
        shipping_type = "ground"
        break
    elif shipping_type == "2" or shipping_type == "drone":
        shipping_type = "drone"
        break
    else:
        print("Please enter either '1' for Ground or '2' for Drone.")

# Ground Shipping
if shipping_type == "ground":
    # Loop for selecting Ground shipping method (regular or premium)
    while True:
        try:
            ground_shipping_type = int(input("Enter the shipping speed:\n 1. Regular ground shipping \n 2. Premium shipping:\n "))
            if ground_shipping_type == 1:
                selected_flat_charge = 20.00
                break
            elif ground_shipping_type == 2:
                selected_flat_charge = 125.00  # Premium shipping flat charge
                break
            else:
                print("Enter a valid method of shipping (1 or 2).")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

    # Determine price per pound for Ground shipping
    if weight <= 2:
        ground_price_per_pound = 1.50
    elif weight <= 6:
        ground_price_per_pound = 3.00
    elif weight <= 10:
        ground_price_per_pound = 4.00
    else:
        ground_price_per_pound = 4.75

    ground_cost = calculate_shipping(weight, ground_price_per_pound, selected_flat_charge)
    print(f"Ground shipping cost is ${ground_cost:.2f}.")

# Drone Shipping
elif shipping_type == "drone":
    # Determine price per pound for Drone shipping
    if weight <= 2:
        drone_price_per_pound = 4.50
    elif weight <= 6:
        drone_price_per_pound = 9.00
    elif weight <= 10:
        drone_price_per_pound = 12.00
    else:
        drone_price_per_pound = 14.25

    drone_cost = calculate_shipping(weight, drone_price_per_pound, 0.00)  # No flat charge for drone shipping
    print(f"Drone shipping cost is ${drone_cost:.2f}.")

# Calculate costs for all shipping methods
# Ground shipping (regular)
if weight <= 2:
    ground_regular_price_per_pound = 1.50
elif weight <= 6:
    ground_regular_price_per_pound = 3.00
elif weight <= 10:
    ground_regular_price_per_pound = 4.00
else:
    ground_regular_price_per_pound = 4.75

ground_regular_cost = calculate_shipping(weight, ground_regular_price_per_pound, 20.00)

# Ground shipping (premium)
if weight <= 2:
    ground_premium_price_per_pound = 1.50
elif weight <= 6:
    ground_premium_price_per_pound = 3.00
elif weight <= 10:
    ground_premium_price_per_pound = 4.00
else:
    ground_premium_price_per_pound = 4.75

ground_premium_cost = calculate_shipping(weight, ground_premium_price_per_pound, 125.00)

# Drone shipping (all weights)
if weight <= 2:
    drone_price_per_pound = 4.50
elif weight <= 6:
    drone_price_per_pound = 9.00
elif weight <= 10:
    drone_price_per_pound = 12.00
else:
    drone_price_per_pound = 14.25

drone_cost = calculate_shipping(weight, drone_price_per_pound, 0.00)

# Print all possible costs for comparison
print("\nShipping options for your package:")
print(f"Regular Ground Shipping: ${ground_regular_cost:.2f}")
print(f"Premium Ground Shipping: ${ground_premium_cost:.2f}")
print(f"Drone Shipping: ${drone_cost:.2f}")

# Find the cheapest shipping method
cheapest_cost = min(ground_regular_cost, ground_premium_cost, drone_cost)

# Let the user know if the shipping method they chose was the cheapest
if shipping_type == "ground":
    if selected_flat_charge == 20.00 and ground_regular_cost == cheapest_cost:
        print("You chose the cheapest shipping method: Regular Ground Shipping.")
    elif selected_flat_charge == 125.00 and ground_premium_cost == cheapest_cost:
        print("You chose the cheapest shipping method: Premium Ground Shipping.")
    else:
        print("Your selected Ground shipping is not the cheapest option.")
elif shipping_type == "drone":
    if drone_cost == cheapest_cost:
        print("You chose the cheapest shipping method: Drone Shipping.")
    else:
        print("Your selected Drone shipping is not the cheapest option.")

# Ask the user if they want to change their shipping option
change_option = input("\nWould you like to change your shipping method to a different option? (yes/no): ").lower()

if change_option == "yes":
    # Present the cheaper options based on the lowest price
    print(f"The lowest option currently is:")
    if cheapest_cost == ground_regular_cost:
        print("Regular Ground Shipping.")
    elif cheapest_cost == ground_premium_cost:
        print("Premium Ground Shipping.")
    elif cheapest_cost == drone_cost:
        print("Drone Shipping.")

    # Ask the user to choose a new shipping method
    new_shipping = input("Which shipping option would you like to choose?\n 1. Regular Ground\n 2. Premium Ground\n 3. Drone\n ").strip()

    # Reassign and recalculate the shipping method and cost based on new choice
    if new_shipping == "1":
        shipping_type = "ground"
        selected_flat_charge = 20.00
        # Recalculate the cost for the selected shipping method
        ground_cost = calculate_shipping(weight, ground_regular_price_per_pound, 20.00)
        print(f"You have selected Regular Ground Shipping. New cost: ${ground_cost:.2f}")
    elif new_shipping == "2":
        shipping_type = "ground"
        selected_flat_charge = 125.00
        # Recalculate the cost for the selected shipping method
        ground_cost = calculate_shipping(weight, ground_premium_price_per_pound, 125.00)
        print(f"You have selected Premium Ground Shipping. New cost: ${ground_cost:.2f}")
    elif new_shipping == "3":
        shipping_type = "drone"
        # Recalculate the cost for the selected shipping method
        drone_cost = calculate_shipping(weight, drone_price_per_pound, 0.00)
        print(f"You have selected Drone Shipping. New cost: ${drone_cost:.2f}")
    else:
        print("Invalid selection. Please choose a valid option.")

    # Confirm the new shipping method and cost
    new_cost = ground_cost if shipping_type == "ground" else drone_cost
    print(f"Your new shipping method is {shipping_type.capitalize()} Shipping with a total cost of ${new_cost:.2f}. Your package will be shipped shortly!")
elif change_option == "no":
    print("You have kept your original shipping choice. Your package will be shipped shortly!")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
