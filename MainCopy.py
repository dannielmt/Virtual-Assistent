import speech_recognition as sr 
import pyttsx3, pywhatkit, datetime, wikipedia, pyjokes, webbrowser


webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))

s = webbrowser.get('firefox')


name = 'alexa'

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


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


        

run()