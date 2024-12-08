# Echo chatbot that repeats everything the user says

print("Hello! Welcome to the Echo chatbot!")
print("I am a chatbot and not a human.\nI will repeat whatever you tell me.\nType 'exit' at any time to end the program.")

# Ask for the user's name
user_name = input("What's your name? ")

# The open brackets and .format allow to insert the user input/name
print("Nice to meet you, {}! Let's chat.".format(user_name))

while True:
    print("\nEnter in a prompt you want the chatbot to repeat:")
    
    # Prompt user to enter something for the program to repeat
    stuff_to_echo = input()  # Store user input in the stuff_to_echo variable
    
    # Check if the user wants to exit the chat
    if stuff_to_echo.lower() == "exit":  # Case-insensitive check for 'exit'
        print("Thanks for talking with me, {}! Goodbye!".format(user_name))
        break  # Exit the loop if the user types 'exit'
    
    # Add some fun responses for certain inputs
    elif "hello" in stuff_to_echo.lower():
        print("Hello, {}! How's your day going?".format(user_name))
    
    elif "how are you" in stuff_to_echo.lower():
        print("I'm just a chatbot, {}, but I’m doing great! How about you?".format(user_name))
    
    elif "joke" in stuff_to_echo.lower():
        print("Why don't skeletons fight each other? Because they don't have the guts!")
    
    else:
        print("{}, you said: {}".format(user_name, stuff_to_echo))
