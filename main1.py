import pyttsx3

if __name__=="__main__":
    print("Welcome to robospeaker 1.1 created by Annu")
    x= input("enter what you want to speak:")
    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()
    