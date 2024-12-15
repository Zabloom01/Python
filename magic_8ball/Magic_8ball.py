# This is the traditional magic 8-ball script with if, elif, else statements.

import random  # Import random library to allow for .randint() function

# Optional: Ask for the user's name, or you can keep it as a fixed name
name = input("What is your name? (Leave blank to skip)\n").strip()
if name == "":
    name = "User"

print(f"Hello, {name}! Welcome to the Magic 8-Ball. Ask your questions, or type 'exit' to leave.\n")

# Set While loop to true for an infinite loop to allow user to keep asking questions
while True:
    # Prompt the user to ask a question
    question = input(f"{name}, what do you want to ask the magic 8-ball?\n").strip() # .strip() removes spaces before and after input
    
    # Check if the user wants to exit
    if question.lower() == "exit":
        print("Thanks for playing! Goodbye.")
        break  # Exit the loop
    
    # Check if the question is valid (not empty)
    if question == "":
        print("You need to ask a question to get an answer!\n")
    else:
        # Generate a random number between 1 and 9
        random_number = random.randint(1, 9)
        
        # Use if, elif, and else to determine the response
        if random_number == 1:
            response = "Yes - definitely"
        elif random_number == 2:
            response = "It is decidedly so"
        elif random_number == 3:
            response = "Without a doubt"
        elif random_number == 4:
            response = "Reply hazy, try again"
        elif random_number == 5:
            response = "Ask again later"
        elif random_number == 6:
            response = "Better not tell you now"
        elif random_number == 7:
            response = "My sources say no"
        elif random_number == 8:
            response = "Outlook not so good"
        else:  # random_number == 9
            response = "Very doubtful"
        
        # Print the user's question and the 8-ball's response
        print(f"\n{name} asked: {question}")
        print(f"Magic 8-ball says: {response}\n")

