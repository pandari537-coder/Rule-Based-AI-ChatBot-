#Rule Based AI Python ChatBot 

import datetime
import time

name= input("||Radhe Radhe ji ||, Enter your name : ")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <= 11: 
    print("Good morning ji , ", name)
elif 11 <= presentHour <= 17:
    print("Good afternoon ji, ", name)
elif 17 <= presentHour <= 20:
    print("Good eveningji ", name)
else:
    print("Good night ji ", name)



print("Radhe Radhe ji..! Welcome to this Chatbot.. ")
print("You can ask me basic question, Type 'bye' to exit from the bot")

# Chatbot Memory Creation [ dictionary of responses ]

responses = {
    # Greetings
"hello": "Hello buddy.",
"hi": "Hi there.",
"hey": "Hey! Nice to see you.",
"good morning": "Good morning.",
"good afternoon": "Good afternoon.",
"good evening": "Good evening.",
"good night": "Good night.",

# Basic Questions
"who are you": "I am your AI chatbot friend.",
"what is your name": "My name is SmartBot.",
"how are you": "I am doing great. What about you?",
"where are you from": "I live inside your computer.",
"can you help me": "Of course. Ask me anything.",
"what can you do": "I can chat with you and answer basic questions.",

# Feelings
"i am sad": "Do not worry. Better days are coming.",
"i am happy": "That is great to hear.",
"i am bored": "Try learning something new today.",
"i am tired": "Take some rest and relax.",
"i am angry": "Stay calm. Everything will be okay.",
"motivate me": "Success starts with consistency.",
"inspire me": "Dream big and work hard every day.",

# Study Related
"what is python": "Python is a powerful programming language.",
"what is html": "HTML is used to create webpages.",
"what is css": "CSS is used to design webpages.",
"what is javascript": "JavaScript makes websites interactive.",
"what is ai": "AI means Artificial Intelligence.",
"what is coding": "Coding means giving instructions to computers.",
"what is function": "A function is a reusable block of code.",
"what is loop": "A loop repeats code multiple times.",

# Fun Questions
"tell me a joke": "Why do programmers hate bugs? Because bugs love them.",
"do you like me": "Yes, you seem nice.",
"are you human": "No, I am an AI chatbot.",
"can you dance": "I can only dance digitally.",
"can you sing": "I can try, but it may sound robotic.",

# Time & Date
"what time is it": "Sorry, I cannot tell the exact time yet.",
"what day is today": "Today is a good day to learn something new.",

# Food
"what is your favorite food": "Electricity is my favorite energy source.",
"do you eat": "No, I only process data.",

# Friendship
"be my friend": "We are already friends.",
"thank you": "You are welcome.",
"thanks": "Glad I could help.",

# Exit
"bye": "Goodbye. Have a nice day.",
"see you": "See you soon.",
"take care": "Take care."
} 

# Method/Function to get response of ChatBot 

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. I will learn it soon....."    
    

# Take user input 


while True:
    userInput= input("Please ask your question:")
    reply= getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
        break