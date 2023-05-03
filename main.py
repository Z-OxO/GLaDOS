import openai
import configparser
from colorama import Fore
from pyaudio import *
import speech_recognition as sr
import pyttsx3
import os


# Charge la clé API OpenAI depuis la configuration
config = configparser.ConfigParser()
config.read("config.ini")
openai.api_key = config["openai"]["api_key"]
languageconfig = config["language"]["lang"]



if not os.path.exists("Conversation"):
    os.makedirs("Conversation")
file = os.path.join("Conversation", "conversation.txt")
if not os.path.exists(file):
    with open(file, "a+") as fichier:
        fichier.write("Tu dois prendre en compte de ces infomation pour repondre à la prochaine question(si rien est ecrit après cette phrase ignore la):")
with open(file,"w") as fichier:
    fichier.write("")
    print(Fore.LIGHTCYAN_EX+"Conversations have been deleted to free up memory")


def Menu():
    pass


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty("voice","fr-FR")
    engine.say(text)
    engine.runAndWait()


def Gpt_turbo():
    with open(file,"r",encoding='utf-8')as fichier:
        fichier_content = fichier.read()
    audio = audio_reconize()
    print("GLaDOS thinks ...")
    try:
        completion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role': 'user', 'content': fichier_content+audio}
        ],
        temperature = 0
        )
    except openai.InvalidRequestError as e:
        print(Fore.LIGHTRED_EX+"Your conversations are too long or Error when requesting Openai API (Conversations automatically deleted)")
        with open(file,"w") as file_content:
            file_content.write('')     
        exit("{0}".format(e))
    completion = completion['choices'][0]['message']['content']
    print(Fore.LIGHTMAGENTA_EX+"GLaDOS ----> ",completion+Fore.RESET)
    text_to_speech(completion)
    with open(file,"+a",encoding='utf-8') as fichier:
        fichier.write("User question:"+audio+"\nReponse from GLaDOS:\n"+completion+"\n")  
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
        text = r.recognize_google(audio, language=str(languageconfig))
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
