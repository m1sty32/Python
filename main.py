import pyttsx3

def say_sentence(sentence):
    engine = pyttsx3.init()
    engine.say(sentence)
    engine.runAndWait()
    
say_sentence("Привет,как дела?")