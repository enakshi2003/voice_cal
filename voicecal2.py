import pyttsx3
import datetime
import speech_recognition as sr
import operator
import playsound
import wolframalpha
import webbrowser
import os
import smtplib
from self import self

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am a voice Calculator . Please tell me how may I help you")


def takeCommand():
    # It take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


# def get_operator_fn(op):
#     return{
#         '+' : operator.add,
#         '-' : operator.sub,
#         '*' : operator.mul,
#         'divided': operator.__truediv__
#             }[op]
# def eval_binary_expr(op1, oper, op2):
#     op1,op2 = int(op1), int(op2)
#     return get_operator_fn(oper)(op1, op2)
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'do some calculation' in self.query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("What you want to calculate")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)


def get_operator_fn(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        'divided': operator.__truediv__
    }[op]


def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)
    speak("Your result is..")
    speak(eval_binary_expr(*(my_string.split())))
