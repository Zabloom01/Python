def is_valid_weight(weight_str):
    """
    Check if the input string is a valid number (integer or decimal).
    """
    try:
        float(weight_str)  # Convert string to float
        return True
    except ValueError:
        return False


def main():
    weight_attempts = 0  # Initialize counter for invalid weight attempts
    planet_attempts = 0  # Initialize counter for invalid planet attempts
    
    # Ask the user how much they weigh
    while weight_attempts < 5: # exits program if more than 5 incorrect attemps
        try:
            weight_input = input("How much do you weigh (in lbs)? \n")
        except EOFError: # If Python ends unexpectedly because it waited and did not get an input
            print("Input ended unexpectedly. Goodbye!")
            return  # Exit the program
        
        # Validate the weight input
        if is_valid_weight(weight_input):
            weight = float(weight_input)  # Convert valid string to float
            break
        else:
            print("Invalid input for weight. Please enter a valid number.")
            weight_attempts += 1  # Increment attempt counter
    else:
        print("Too many invalid attempts for weight. Goodbye!")
        return  # Exit the program
    
    # Ask user what planet they are traveling to.
    valid_planets = ["MERCURY", "VENUS", "MARS", "JUPITER", "SATURN", "URANUS", "NEPTUNE"]
    
    while planet_attempts < 5:
        try:
            planet = input("What planet are you traveling to? \n").strip().upper()  # Remove trailing and leading whitespaces (e.g., spaces, indents, etc.) and convert to uppercase
        except EOFError:
            print("Input ended unexpectedly. Goodbye!")
            return  # Exit the program
        
        if planet in valid_planets:
            break  # Valid planet input, exit loop
        else:
            print("Sorry, I don't recognize that planet. Please enter a valid planet name.")
            planet_attempts += 1  # Increment planet attempt counter
    else:
        print("Too many invalid attempts for planet. Goodbye!")
        return  # Exit the program
    
    # Print the planet they chose
    print(f"The planet you chose is {planet}!")
    
    # Calculate the weight based on the planet's gravity
    """
    Create dictionary and assign variables.
    """
    gravity_factors = {
        "MERCURY": 0.38,
        "VENUS": 0.91,
        "MARS": 0.38,
        "JUPITER": 2.34,
        "SATURN": 1.06,
        "URANUS": 0.92,
        "NEPTUNE": 1.19
    }
    
    if planet in gravity_factors:
        adjusted_weight = weight * gravity_factors[planet]
        print(f"On {planet.capitalize()} you weigh {adjusted_weight:.2f} pounds.")


if __name__ == "__main__":
    main()
