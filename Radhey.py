import pyautogui
import pyttsx3                          #speak
import speech_recognition as sr         #take command
import datetime                         #for date and time
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import time
from googletrans import Translator
from tkinter import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM"
engine.setProperty('voice',voices[1].id)
#engine.setProperty('rate',130)
#engine.setProperty('volume',1.0)



def speak(audio):
    if language=='hindi':
        tr = Translator()
        # translate text
        translated_text = tr.translate(audio, src='en', dest='hi')
        engine.say(translated_text.text)
        engine.runAndWait()
    elif language=='english':
        engine.say(audio)
        engine.runAndWait()

def takecommand():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.pause_threshold = 1
        audio = listener.listen(source)#,timeout=1,phrase_time_limit=7)
    try:
        print("Recognizing...")
        command = listener.recognize_google(audio,language='en-in')
        print("User said: " +command)
    except Exception as e:
        speak("Say That Again")
        #return takecommand()
    return command

def wish():
    i = int(datetime.datetime.now().hour)
    if i>=0 and i<=12:
        speak("Good Morning")
    elif i>12 and i<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("Hello MRP , Radhey Here . what can i do for you ?")

def gt(t,sl,tt):
    #initialize the Translator
    translator = Translator()

    text = t
    source_lan = sl
    translated_to = tt
    #translate text
    translated_text = translator.translate(text, src=source_lan, dest = translated_to)
    print(f"The Actual Text was {text}")
    print(f"The Translated Text is: {translated_text.text}")
    print(f"The Translated Text pronunciation is {translated_text.pronunciation}")
    speak(translated_text.text)

def do():
    wish()
    while True:
        cmd = takecommand().lower()

    #Logic Building for Tasks

        if 'open command prompt' in cmd:
            os.system("start cmd")
            speak("okay")

        elif 'open notepad' in cmd:
            path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)
            speak("okay")

        elif 'close notepad' in cmd:
            path = "C:\\Windows\\system32\\notepad.exe"
            os.system("taskkill /f /im notepad.exe")
            speak("okay")

        elif 'open word' in cmd:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
            os.startfile(path)
            speak("okay")

        elif 'open excel' in cmd:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe"
            os.startfile(path)
            speak("okay")

        elif 'open powerpoint' in cmd:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
            os.startfile(path)
            speak("okay")

        elif 'open this computer' in cmd:
            speak("which drive do you want to open ?")
            drive=takecommand().lower()
            if 'c' in drive:
                os.startfile("C:")
            elif'd' in drive:
                os.startfile("D:")
            elif'e' in drive:
                os.startfile("E:")
            elif'f' in drive:
                os.startfile("F:")

        elif 'exit' in cmd:
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')

        elif 'music' in cmd:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

        elif 'ip address' in cmd:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak("your ip address is :" +ip)

        elif 'wikipedia' in cmd:
            cmd = cmd.replace("wikipedia","")
            result = wikipedia.summary(cmd,sentences=1)
            speak("according to wikipedia")
            speak(result)

        elif'kya hai' in cmd:
            cmd = cmd.replace("kya hai","")
            result = wikipedia.summary(cmd,sentences=1)
            speak("according to wikipedia")
            speak(result)

        elif 'open youtube' in cmd:
            webbrowser.open("www.youtube.com")

        elif 'open google' in cmd:
            speak("what should i search on google?")
            s = takecommand().lower()
            pywhatkit.search(s)

        elif 'search' in cmd:
            import wikipedia as googleScrap
            cmd = cmd.replace('search','')
            speak("ok searching")
            try:
                pywhatkit.search(cmd)
                result = googleScrap.summary(cmd,2)
                gt(result,'en','hi')
            except:
                speak("no data found")

        elif 'translate' in cmd:
            speak("from which language you want to translate?")
            SL = takecommand().lower()
            speak("to which language you want to translate?")
            TT = takecommand().lower()
            speak("okay, what is the sentence ?")
            sentence = takecommand()

            if 'english' in SL:
                SL = "en"
            elif'hindi' in SL:
                SL = "hi"
            elif 'gujarati' in SL:
                SL = "gu"

            if 'english' in TT:
                SL = "en"
            elif 'hindi' in TT:
                SL = "hi"
            elif 'gujarati' in TT:
                SL = "gu"
            gt(sentence,SL,TT)


        elif 'on youtube' in cmd:
            song = cmd.replace('on youtube', '')
            song = cmd.replace('play','')
            speak("ok playing")
            print(song)
            pywhatkit.playonyt(song)


        elif 'send message' in cmd:
            speak("whom you want to send message?")
            person=takecommand().lower()
            speak("ok, what is the message?")
            msg=takecommand()
            if 'mihir' in person:
                pywhatkit.sendwhatmsg_instantly('+919016158092',msg)
            elif 'ved' in person:
                pywhatkit.sendwhatmsg_instantly('+918849254855',msg)
            elif 'romin' in person:
                pywhatkit.sendwhatmsg_instantly('+919898593128', msg)
            elif 'priya' in person:
                pywhatkit.sendwhatmsg_instantly('+918153841373', msg)
            elif 'papa' in person:
                pywhatkit.sendwhatmsg_instantly('+919428222879', msg)
            elif 'mummy' in person:
                pywhatkit.sendwhatmsg_instantly('+919327693580', msg)
            elif 'viral' in person:
                pywhatkit.sendwhatmsg_instantly('+919726408336', msg)
            elif 'sp' in person:
                speak("you dont have her Whatsapp Number. you have to request queen of the heaven to give her whatsapp number")

            else:
                speak("no contact found")


        elif 'time' in cmd:
            t = datetime.datetime.now().strftime('%I:%M %p')
            speak("current time is :" + t)

        elif 'shutdown pc' in cmd:
            speak("ok shuting down pc")
            os.system("shutdown /s /t 5")

        elif 'restart pc' in cmd:
            speak("ok restarting pc")
            os.system("shutdown /r /t 5")

        elif 'open' in cmd:
            speak("please repeat ,what should i open.")
            continue

        elif 'are you single' in cmd:
            speak("No . i am in relationship with wifi")
        elif 'what are you doing' in cmd:
            speak("i am currently running your tasks, and listening your dumb questions")
        elif 'do you love me' in cmd:
            speak("yeah of course. you are very kind person MRP")
        elif 'i love you' in cmd:
            speak('i love you too MRP, but as a programmer')
        elif'feeling not good' in cmd:
            speak("you should take a break from daily life")

        elif 'you can sleep' in cmd:
            speak("thanks for using. i am always here for you, you can call me anytime.")

            break

        time.sleep(7)
        speak("now what should i do ?")

# print("which language")
# Creating the tkinter window
root = Tk()
root.geometry("400x300+700+250")
def hindi():
    global language
    language = 'hindi'
    root.destroy()
def english():
    global language
    language = 'english'
    root.destroy()
a = Button(root, text="Eng",command=english,padx=50,pady=20)
a.pack(side='left')
b = Button(root, text="Hindi",command=hindi,padx=50,pady=20)
b.pack(side='right')
root.mainloop()
do()