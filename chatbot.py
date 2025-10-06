import random

print("Welcome to Smart Chatbox! Type 'exit' to quit.\n")


responses = {
    "hi": ["Hello! How are you?", "Hi there! Nice to meet you!"],
    "hello": ["Hi!", "Hello! How can I help you?"],
    "how are you": ["I'm just a program, but I'm doing great!", "Feeling code-tastic!"],
    "what is your name": ["I am a Python Chatbot.", "You can call me PyBot."],
    "bye": ["Goodbye! Have a nice day!", "See you later!"],
}


default_responses = [
    "Sorry, I don't understand that.",
    "Can you rephrase that?",
    "Hmm, interesting!",
    "I am not sure how to respond to that."
]

while True:
    user_input = input("You: ").lower() 

    if user_input == "exit":
        print("Chatbot: Bye! ")
        break
    elif user_input in responses:
      
        print("Chatbot:", random.choice(responses[user_input]))
    else:
        print("Chatbot:", random.choice(default_responses))
