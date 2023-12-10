#!/usr/bin/env python
# coding: utf-8

# In[4]:


import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hello' in command:
                command = command.replace('hello', '')
                print(command)
    except:
        pass
    return command

def respond_to_greeting():
    responses = [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
        "Greetings! What do you need assistance with?"
    ]
    talk(responses[0]) 
    
def run_hello():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'how are you' in command:
        talk("I'm doing well, thank you! How can I assist you today?")
    else:
        talk('Please say the command again.')


while True:
    run_hello()


# In[ ]:




