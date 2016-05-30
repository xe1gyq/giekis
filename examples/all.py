import speech_recognition as sr
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "hello.wav")
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source) # read the entire audio file
print("Google Speech Recognition thinks you said " + r.recognize_google(audio, key="AIzaSyD1o305c7liSJzZUS46OIOxig92ViUCbAQ"))
WIT_AI_KEY = ""
print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
