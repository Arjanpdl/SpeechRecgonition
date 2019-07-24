import  speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

with sr.Microphone() as source:
    engine = pyttsx3.init()
    engine.say('I am listening and I can do anything')
    engine.runAndWait()
    print("Speak")
    audio = r.listen(source)

    text = r.recognize_google(audio)
    print("You said : {}".format(text).upper())

    if(format(text).upper() == "HELLO"):
        engine = pyttsx3.init()
        engine.say('Hello')
        engine.runAndWait()

    elif (format(text).upper() == "I LOVE YOU"):
        engine = pyttsx3.init()
        engine.say('I love you too')
        engine.runAndWait()

    elif (format(text).upper() == "HI"):
        engine = pyttsx3.init()
        engine.say('Hi')
        engine.runAndWait()

    elif (format(text).upper() == "I AM IDIOT"):
        engine = pyttsx3.init()
        engine.say('Yes')
        engine.runAndWait()

    else:
        print("Bye")
        engine = pyttsx3.init()
        engine.say('Are you idiot hahah! I am still developing donot ask me complex question')
        engine.runAndWait()





