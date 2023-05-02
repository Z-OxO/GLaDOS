import openai
import configparser
from colorama import Fore
from pyaudio import *
import speech_recognition as sr
import pyttsx3


# Charge la clé API OpenAI depuis la configuration
config = configparser.ConfigParser()
config.read("config.ini")
openai.api_key = config["openai"]["api_key"]


def Menu():
    pass


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def Gpt_turbo():
    content = audio_reconize()
    print("GLaDOS thinks ...")
    completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'user', 'content': content}
    ],
    temperature = 0  
    )
    completion = completion['choices'][0]['message']['content']
    print(Fore.LIGHTMAGENTA_EX+"GLaDOS ----> ",completion+Fore.RESET)
    text_to_speech(completion)
    while True:
        choice = input("Another request? (y or n)")
        if choice == "y":
            Gpt_turbo()
        elif choice == "n":
            Menu()
        else:
            print(Fore.RED,"Invalid input")


def audio_reconize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.LIGHTCYAN_EX,"Speak into your microphone to ask a question to GLaDOS ---->",Fore.RESET)
        audio = r.listen(source)
    # Conversion audio en texte
    try:
        text = r.recognize_google(audio, language='fr-FR')
        print(Fore.LIGHTCYAN_EX,"You said : " + text)
        while True:
            choice_audio=""
            choice_audio = input("Submit to GLaDOS ? (y or n): ")
            if choice_audio == "y":
                return text
            elif choice_audio =="n":
                audio_reconize()
    except sr.UnknownValueError:
        print(Fore.LIGHTRED_EX,"GLaDOS did not understand what you said. Retry please",Fore.RESET)
        Gpt_turbo()
    except sr.RequestError as e:
        exit(Fore.LIGHTRED_EX,"Error when requesting the speech recognition service :{0}".format(e))
        
Gpt_turbo()
