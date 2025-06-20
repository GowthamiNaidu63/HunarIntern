import datetime

def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        # Rule-based responses
        if user_input in ["hi", "hello"]:
            print("Chatbot: Hello there! How can I help you?")
        elif "weather" in user_input:
            print("Chatbot: The weather is sunny with a chance of code!")
        elif "name" in user_input:
            print("Chatbot: I'm ChatGPT, your friendly chatbot.")
        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M")
            print(f"Chatbot: The current time is {current_time}.")
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that.")

# Run the chatbot
chatbot()
