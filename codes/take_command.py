import pywhatkit
import speech_recognition as sr



def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command

def start():
    x = listen()
    if 'radhe' in x:
        print(x)
        return take_command()
    else:
        print("Kindly Mention Proper Name")

def take_command():
    print("What can I do for You?")
    cmd = listen()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play','')
        print("ok playing")
        print(song)
        pywhatkit.playonyt(song)
    elif 'heart' or 'dil' in cmd:
        import heart.py
        print("ok drawing heart")
        exec("heart.py")
start()
