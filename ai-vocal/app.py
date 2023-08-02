from speech2text import list_microphone, speech_to_text
from text2speech import google_text_to_speech
from gpt import ask_gpt

# getting the right microphone
# list_microphone()

input = speech_to_text()
google_text_to_speech(ask_gpt(input))