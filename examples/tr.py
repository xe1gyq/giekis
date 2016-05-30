import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

with sr.Microphone(4) as source:
    print("Say something!")
    audio = r.listen(source)

print "Done listening!"

print "You said: " + r.recognize(audio)
