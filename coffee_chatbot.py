# Define your functions
def coffee_bot():
    print("Welcome to the cafe! I am your personal Coffee Bot! Prepare yourself for an unforgettable drink experience!")
    customer_name = input("First, what's your name? ")
    print(f"Hello, {customer_name}! Let’s get your order started!")

    size = get_size()  # Get the drink size
    if size:  # If a valid size is selected
        print(f"Ah, {customer_name}, you've selected a {size} drink. Bold choice!")
        drink_type = get_drink_type()  # Get the drink type (e.g., brewed coffee, mocha, latte)
        if drink_type:  # Check if a valid drink type is selected
            print(f"Excellent taste, {customer_name}! You've selected a {drink_type}. But wait, there's more... Let's talk milk!")
            milk_type = order_latte()  # Get the milk type (if applicable)
            if milk_type:
                temperature = get_temperature()  # Ask if they want it hot or iced
                whipped_cream = ask_whipped_cream()  # Ask if they want whipped cream
                total_cost = calculate_cost(size, drink_type, milk_type, temperature, whipped_cream)
                print(f"Your {drink_type} with {milk_type} milk, served {temperature}, and {'with' if whipped_cream else 'without'} whipped cream is now complete, {customer_name}.")
                print(f"Thanks for visiting, {customer_name}. Your {drink_type} will be out shortly!")
                print(f"The total cost of your order is ${total_cost:.2f}")

def get_size():
    print("Enter 'clear' or 'exit' at any time to end your order. But why would you want to leave? We’re just getting started!")
    count = 0  # Initialize count variable
    while count < 6:  # Allow up to 5 failed attempts
        res = input("What size drink can I get for you? Choose wisely...\n[a] Small (It's cute)\n[b] Medium (The Goldilocks choice)\n[c] Large (For the adventurous)\n> ").lower()

        if res == 'a':
            return 'small'
        elif res == 'b':
            return 'medium'
        elif res == 'c':
            return 'large'
        elif res == "clear" or res == "exit":
            print("Your order has ended! Thank you for wasting my time... I mean, thank you for visiting!")
            return None

        # Error handling messages with humor
        if count == 1:
            print("Come on, pick one! It’s not rocket science. Just choose a letter: a, b, or c.")
        elif count == 2:
            print("You’re testing my patience here... I’ll let you have one more shot!")
        elif count == 3:
            print("Alright, listen up! I’m about to lose it. You have two more chances before I call in backup...!")
        elif count == 4:
            print("This is your last warning! I swear, if you pick 'd', I’m shutting down.")

        count += 1  # Increment count after each failed attempt

    print("Sorry, you've made too many incorrect attempts. You're out of here!")
    return None  # Return None after too many invalid attempts

def get_drink_type():
    count = 0  # Initialize count for the number of attempts
    while count < 6:  # Allow up to 5 failed attempts
        res = input("What type of drink would you like? Time to make your choice...\n[a] Brewed Coffee (For the serious)\n[b] Mocha (For the sweet-tooths)\n[c] Latte (Because you’re fancy)\n> ").lower()

        if res == 'a':
            return 'Brewed Coffee'
        elif res == 'b':
            return 'Mocha'
        elif res == 'c':
            return 'Latte'
        elif res == "clear" or res == "exit":
            print("Your order has ended! Thank you for your indecisiveness!")
            return None

        # Error handling messages with humor
        if count == 1:
            print("I said a, b, or c! Not the alphabet soup!")
        elif count == 2:
            print("Is there a secret menu I don’t know about? Just pick one, please!")
        elif count == 3:
            print("The suspense is killing me. Choose your drink, or I’ll choose for you! Spoiler alert: It’ll be water.")
        elif count == 4:
            print("Alright, alright! You've made this harder than it should be. One more shot!")
        
        count += 1  # Increment count after each failed attempt

    print("Sorry, you've made too many incorrect attempts. Exiting. You’ve disappointed us both.")
    return None  # Return None after too many invalid attempts

def order_latte():
    count = 0  # Initialize count for milk choices
    while count < 6:  # Allow up to 5 failed attempts
        res = input("And what kind of milk for your latte? Make it count...\n[a] 2% (Just the basics)\n[b] Non-fat milk (Oh, you're healthy...)\n[c] Soy milk (For the trendy folks)\n> ").lower()

        if res == 'a':
            return '2%'
        elif res == 'b':
            return 'Non-fat'
        elif res == 'c':
            return 'Soy'
        elif res == "clear" or res == "exit":
            print("Your order has ended! I’ll miss you, but not really.")
            return None

        # Error handling messages with humor
        if count == 1:
            print("You’re not fooling me with that 'd' option. It’s a no-go!")
        elif count == 2:
            print("Let’s not complicate this. Choose a letter. We’re friends now, right?")
        elif count == 3:
            print("I see you're trying to test my patience. But it’s no match for my code.")
        elif count == 4:
            print("Last warning! If you mess this up, I’ll just give you air instead of milk.")
        
        count += 1  # Increment count after each failed attempt

    print("Sorry, you've made too many incorrect attempts. Time’s up!  Your order has ended, next customer please!")
    return None  # Return None after too many invalid attempts

def get_temperature():
    count = 0  # Initialize count for temperature choices
    while count < 6:  # Allow up to 5 failed attempts
        res = input("Would you like your drink hot or iced?\n[a] Hot (Warm and cozy!)\n[b] Iced (Cool and refreshing!)\n> ").lower()

        if res == 'a':
            return 'hot'
        elif res == 'b':
            return 'iced'
        elif res == "clear" or res == "exit":
            print("Your order has ended! Hope to see you again soon!")
            return None

        # Error handling messages with humor
        if count == 1:
            print("Come on, hot or iced, pick one!")
        elif count == 2:
            print("Not sure if you want hot or iced? Let's move it along.")
        elif count == 3:
            print("Alright, let's speed this up! Hot or iced, just choose one.")
        elif count == 4:
            print("This is your last chance! Hot or iced, that's all you get.")

        count += 1  # Increment count after each failed attempt

    print("Sorry, you've made too many incorrect attempts. You're out of here!")
    return None  # Return None after too many invalid attempts

def ask_whipped_cream():
    count = 0  # Initialize count for whipped cream question
    while count < 6:  # Allow up to 5 failed attempts
        res = input("Would you like whipped cream on top?\n[a] Yes (Treat yourself!)\n[b] No (You're disciplined!)\n> ").lower()

        if res == 'a':
            return True
        elif res == 'b':
            return False
        elif res == "clear" or res == "exit":
            print("Your order has ended! I’ll miss you, but not really.")
            return None

        # Error handling messages with humor
        if count == 1:
            print("It’s a simple question, yes or no!")
        elif count == 2:
            print("Whipped cream: Yes or No? No need to overthink it!")
        elif count == 3:
            print("Last chance, whipped cream or not? You got this.")
        
        count += 1  # Increment count after each failed attempt

    print("Sorry, you've made too many incorrect attempts. You're out of here!")
    return None  # Return None after too many invalid attempts

def calculate_cost(size, drink_type, milk_type, temperature, whipped_cream):
    # Price mapping for drinks and options
    prices = {
        'small': 2.50,
        'medium': 3.00,
        'large': 3.50,
        'Brewed Coffee': 1.50,
        'Mocha': 2.75,
        'Latte': 3.00,
        '2%': 0.00,
        'Non-fat': 0.00,
        'Soy': 0.50,
        'hot': 0.00,
        'iced': 0.00,
        'whipped_cream': 0.50
    }
    
    # Base drink cost based on size
    total_cost = prices[size] + prices[drink_type]
    
    # Add cost of milk (if applicable)
    if milk_type:
        total_cost += prices[milk_type]
    
    # Add whipped cream cost
    if whipped_cream:
        total_cost += prices['whipped_cream']
    
    return total_cost

# Call coffee_bot()!
coffee_bot()
