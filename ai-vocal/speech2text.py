import speech_recognition as sr

def list_microphone():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# choose the right microphone_index
def speech_to_text():
    microphone_index = 11
    r = sr.Recognizer()
    with sr.Microphone(microphone_index) as source:
        print("Demande moi quelque chose!")
        audio = r.listen(source)
        text = r.recognize_google(audio, None, language="fr-FR")

        print("you> " + text)
        return text