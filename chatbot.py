import re
responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "hey": "Hey! What's up?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "i am fine": "That's great to hear 😊",
    "what is your name": "I am a simple chatbot.",
    "who created you": "I was created by a developer.",
    "what can you do": "I can chat with you and answer simple questions.",
    "help": "Sure! You can ask me basic questions or chat with me.",
    "tell me a joke": "Why did the computer get cold? Because it forgot to close Windows 😂",
    "another joke": "Why do programmers prefer dark mode? Because light attracts bugs 😄",
    "thanks": "You're welcome!",
    "thank you": "Glad I could help 😊",
    "bye": "Goodbye! Have a nice day 👋",
    "good morning": "Good morning! Have a great day ahead ☀️",
    "good evening": "Good evening! How was your day?",
    "where are you from": "I live inside your computer 😄",
    "are you real": "No, I'm just a program, but I can chat with you!",
    "yes": "Great! How can I assist you further?",
    "no": "Alright, let me know if you need anything.",
    "what time is it": "Sorry, I can't access real-time data yet.",
    "what is today's date": "I can't fetch the date, please check your device.",
    "default": "I'm not sure I understand. Could you please rephrase?"
}
# function to find appropriate response based on user's input
def chatbot_response(user_input):
    #convert user input  to lower case to make matching case -insensitive
    user_input=user_input.lower()
    for keyword in responses:
        if keyword == "default":
            continue
        if keyword in user_input: 
            return responses[keyword]
    return responses["default"]

#main function for chatbot
def chatbot():
    print("Chatbot:Hello! I'm here to assist you.(type 'bye' to exit)")
    while True:
        #get user input first
        user_input=input("You : ")
        #if user types'bye', exit loop
        if user_input.lower() =='bye':
            print("chatbot:GoodBye , Have a great day.")
            break

        #get chatbots response based on user input
        reply=chatbot_response(user_input)
        print (f"Chatbot: {reply}")

#run the chatbot
chatbot()