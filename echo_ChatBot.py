# Echo chatbot that repeats everything the user says

print("Hello! Welcome to the Echo chatbot!")
print("This chatbot will repeat everything you say. \nType 'exit' to end the program.")

while True:
    print("Enter in a prompt you want the chatbot to repeat")
    
    # Prompt user to enter something for the program to repeat
    stuff_to_echo = input()  # Store user input in the stuff_to_echo variable
    print("You said:", stuff_to_echo)
    
    # Check if the user wants to exit the chat
    if stuff_to_echo.lower() == "exit":  # Case-insensitive check for 'exit'
        print("Thanks for talking with me! Goodbye!")
        break  # Exit the loop if the user types 'exit'
