import os
import pyttsx3
from gtts import gTTS

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'fr')
    engine.say(text)
    engine.runAndWait()

def google_text_to_speech(text, language='fr', filename='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    os.system('nvlc --no-loop --play-and-exit ' + filename + " && rm " + filename)