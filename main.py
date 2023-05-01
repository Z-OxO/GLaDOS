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

def Gpt_turbo():
    content = audio_reconize()
    completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'user', 'content': content}
    ],
    temperature = 0  
    )
    return print(Fore.LIGHTMAGENTA_EX+"GLaDOS ----> "+completion['choices'][0]['message']['content']+Fore.RESET)


def audio_reconize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dites quelque chose...")
        audio = r.listen(source)
    # Conversion audio en texte
    try:
        text = r.recognize_google(audio, language='fr-FR')
        print("Vous avez dit : " + text)
        return text
    except sr.UnknownValueError:
        print("Je n'ai pas compris ce que vous avez dit.")
    except sr.RequestError as e:
        print("Erreur lors de la requête au service de reconnaissance vocale : {0}".format(e))
        
Gpt_turbo()