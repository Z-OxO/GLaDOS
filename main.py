import openai
import configparser
from colorama import Fore
from pyaudio import *
import speech_recognition as sr
import pyaudio


# Charge la clé API OpenAI depuis la configuration
config = configparser.ConfigParser()
config.read("config.ini")
openai.api_key = config["openai"]["api_key"]


def Menu():
    pass

def Gpt_turbo():
    content = audio_reconize()
    completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'user', 'content': content}
    ],
    temperature = 0  
    )
    print(Fore.LIGHTMAGENTA_EX+"GLaDOS ----> "+completion['choices'][0]['message']['content']+Fore.RESET)
    choice = input("Another request? (y or n)")
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
        print(Fore.RED,"You said : " + text)
        return text
    except sr.UnknownValueError:
        print(Fore.RED,"I did not understand what you said.")
    except sr.RequestError as e:
        print(Fore.RED,"Error when requesting the speech recognition service :{0}".format(e))
        
Gpt_turbo()