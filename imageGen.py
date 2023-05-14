import openai
import configparser
import os
from colorama import Fore
from PIL import Image
import requests
import random
import string

config = configparser.ConfigParser()
config.read("config.ini")
openai.api_key = config["openai"]["api_key"]


def ImageNameGen():
    image_name=""
    for letter in range(1,15):
        image_name += str(random.choice(string.ascii_letters))
    return image_name
    

"""print(Fore.LIGHTCYAN_EX,"Submit an image request to GLaDOS -----> ")
audio_reconize()"""


def ImageGen():
    response = openai.Image.create(
    prompt="",
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    try:
        image_response=requests.get(image_url)
    except:
        exit(Fore.LIGHTRED_EX,"Error while request image URL")
    filename_gen=ImageNameGen()+".png"
    filename=str("imageGen/)"+filename_gen)
    with open(filename,"wb") as f:
        f.write(image_response.content)


ImageGen()