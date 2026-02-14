responses = {
    "1": "How are you?",
    "2": "The weather is cold.",
    "3": "India"
}

print("\nWelcome to Chatbot")

while True:
    print("\nPlease choose an option:")
    print("1. Hello")
    print("2. Weather")
    print("3. Country")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice in responses:
        print("Bot:", responses[choice])

    elif choice == "4":
        print("Bot: Goodbye! Have a great day ")
        break

    else:
        print("Bot: Invalid choice. Please try again.")
