import speech_recognition as sr 
import pyttsx3, pywhatkit, datetime, wikipedia, pyjokes, webbrowser
import pyautogui
from time import sleep 

webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))

s = webbrowser.get('firefox')



name = 'alexa'

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

phone = None

def talk(text):
    engine.say(text)
    engine.runAndWait()




def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, ' ')
                print(rec)
    except:
        pass
    return rec 



def spambot():
    s.open_new(f'https://web.whatsapp.com/send?phone=+{phone}')

    sleep(16)

    with open("LibreriasPrueba\webbrowser\quijote.txt", "r") as file:
        for line in file:
            pyautogui.typewrite(line)
            pyautogui.press("enter")


def run():
    rec = listen()
    if 'play' in rec:
        music = rec.replace('play', ' ')
        talk('Reproduciendo ' + music + 'en youtube')
        pywhatkit.playonyt(music)
    elif 'what time is it' in rec:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " +time)
    elif 'wiki' in rec:
        order = rec.replace('wiki', ' ')
        info = wikipedia.summary(order, 1)
        talk(info)
    elif 'joke' in rec:
        joker = rec.replace('joke', ' ')
        joke = pyjokes.get_joke()
        talk(joke)
    elif 'search' in rec:
        pywhatkit.search(rec)
    elif 'send' in rec:
        sender = rec.replace('send', ' ')
        talk("Enviando mensaje a ", sender)
    elif 'banana' in rec:
        spambot()



        

run()
