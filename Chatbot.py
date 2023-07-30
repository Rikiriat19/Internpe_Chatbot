def get_chatbot_response(user_input):
    # Define chatbot responses for different user inputs
    responses = {
        "hi": "Hello!",
        "hello": "Hi there!",
        "how are you": "I'm doing well, thank you!",
        "what is your name": "I am a chatbot.",
        "bye": "Goodbye! See you soon.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "who created you": "I was created by Ritik using Python.",
        "how old are you": "I am just a program, so I don't have an age.",
        "what is the meaning of life": "The meaning of life is subjective and varies from person to person.",
        "what is the weather": "I'm sorry, I am just a chatbot and cannot provide real-time weather information.",
        "how can I contact support": "For support, you can email us at sharma12jiritk@gmail.com.",
    }
    
    # Check if the user input exists in the responses dictionary
    if user_input.lower() in responses:
        return responses[user_input.lower()]
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

def main():
    # Greeting message
    print("Chatbot: Hi! I am a basic chatbot. You can start chatting with me. Type 'exit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if the user wants to exit the conversation
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! See you soon.")
            break

        # Get the chatbot's response
        response = get_chatbot_response(user_input)
        
        # Print the chatbot's response
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
