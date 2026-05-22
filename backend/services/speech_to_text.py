import speech_recognition as sr

def listen_and_convert():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak your symptoms...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except:
        return "Could not understand audio"