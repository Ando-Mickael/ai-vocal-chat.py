import os
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'fr')
    engine.say(text)
    engine.runAndWait()

def list_microphone():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone(11) as source:
        print("Demande moi quelque chose!")
        audio = r.listen(source)
        text = r.recognize_google(audio, None, language="fr-FR")

        print("you> " + text)
        return text

def chat_with_chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()

    print("chatgpt> " + message)
    return message

# list_microphone()

while(True):
    input = speech_to_text()

    if (input == "close"):
        break

    text_to_speech(chat_with_chatgpt(input))

    print("-----------------\n")