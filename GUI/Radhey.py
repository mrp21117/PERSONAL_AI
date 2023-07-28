import pyautogui
import pyttsx3                          #speak
import speech_recognition as sr         #take command
import datetime                         #for date and time
import os
import random
from requests import get
import wikipedia
import webbrowser
import socket
import pywhatkit
import time
from googletrans import Translator
from tkinter import *
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QTimer)
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUiType
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from Radhey_UI import Ui_MainWindow
import sys


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
        audio = listener.listen(source,timeout=1,phrase_time_limit=7)
    try:
        print("Recognizing...")
        command = listener.recognize_google(audio,language='en-in')
        print("User said: " +command)
    except Exception as e:
        speak("Say That Again")
        return takecommand()
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

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.dotask()

    def takecommand(self):
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            listener.pause_threshold = 1
            audio = listener.listen(source, timeout=1, phrase_time_limit=7)
        try:
            print("Recognizing...")
            command = listener.recognize_google(audio, language='en-in')
            print("User said: " + command)
        except Exception as e:
            speak("Say That Again")
            return takecommand()
        return command

    def dotask(self):
        root = Tk()
        root.geometry("300x150+800+350")
        root.title("Language")
        def hindi():
            global language
            language = 'hindi'
            root.destroy()

        def english():
            global language
            language = 'english'
            root.destroy()
        a = Button(root, text="Eng", command=english, padx=50, pady=20)
        a.pack(side='left')
        b = Button(root, text="Hindi", command=hindi, padx=50, pady=20)
        b.pack(side='right')
        root.mainloop()
        wish()
        while True:
            self.cmd = takecommand().lower()

        #Logic Building for Tasks

            if 'open command prompt' in self.cmd:
                os.system("start cmd")
                speak("okay")

            elif 'open notepad' in self.cmd:
                path = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(path)
                speak("okay")

            elif 'close notepad' in self.cmd:
                path = "C:\\Windows\\system32\\notepad.exe"
                os.system("taskkill /f /im notepad.exe")
                speak("okay")

            elif 'open premiere pro' in self.cmd:
                path = "F:\\APP2022\\Adobe Premiere Pro 2022\\Adobe Premiere Pro.exe"
                os.startfile(path)
                speak("okay opening")

            elif 'open word' in self.cmd:
                path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
                os.startfile(path)
                speak("okay")

            elif 'open excel' in self.cmd:
                path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe"
                os.startfile(path)
                speak("okay")

            elif 'open powerpoint' in self.cmd:
                path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
                os.startfile(path)
                speak("okay")

            elif 'open documents' in self.cmd:
                path = "Documents"
                os.startfile(path)
                speak("okay")

            elif 'open this computer' in self.cmd:
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

            elif 'exit' in self.cmd:
                pyautogui.keyDown('alt')
                pyautogui.press('f4')
                pyautogui.keyUp('alt')

            elif 'music' in self.cmd:
                music_dir = "D:\\Music"
                songs = os.listdir(music_dir)
                rd=random.choice(songs)
                os.startfile(os.path.join(music_dir,rd))

            elif 'ip address' in self.cmd:
                hostname = socket.gethostname()
                ip = socket.gethostbyname(hostname)
                print("PC Name:  " + hostname)
                print("IP Address : " + ip)
                engine.say(ip)
                engine.runAndWait()


            elif 'wikipedia' in self.cmd:
                self.cmd = self.cmd.replace("wikipedia","")
                result = wikipedia.summary(self.cmd,sentences=1)
                speak("according to wikipedia")
                speak(result)
                return result

            elif'kya hai' in self.cmd:
                self.cmd = self.cmd.replace("kya hai","")
                result = wikipedia.summary(self.cmd,sentences=1)
                speak("according to wikipedia")
                speak(result)
                return result

            elif 'open youtube' in self.cmd:
                webbrowser.open("www.youtube.com")

            elif 'open google' in self.cmd:
                speak("what should i search on google?")
                s = takecommand().lower()
                pywhatkit.search(s)

            elif 'search' in self.cmd:
                import wikipedia as googleScrap
                self.cmd = self.cmd.replace('search','')
                speak("ok searching")
                try:
                    pywhatkit.search(self.cmd)
                    result = googleScrap.summary(self.cmd,2)
                    gt(result,'en','hi')
                except:
                    speak("no data found")


            elif 'translate' in self.cmd:
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


            elif 'on youtube' in self.cmd:
                song = self.cmd.replace('on youtube', '')
                song = self.cmd.replace('play','')
                speak("ok playing")
                print(song)
                pywhatkit.playonyt(song)


            elif 'send message' in self.cmd:
                speak("whom you want to send message?")
                person=self.takecommand().lower()
                speak("ok, what is the message?")
                msg=self.takecommand()
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


            elif 'time' in self.cmd:
                t = datetime.datetime.now().strftime('%I:%M %p')
                speak("current time is :" + t)

            elif 'shutdown pc' in self.cmd:
                speak("ok shuting down pc")
                os.system("shutdown /s /t 5")

            elif 'restart pc' in self.cmd:
                speak("ok restarting pc")
                os.system("shutdown /r /t 5")

            elif 'open' in self.cmd:
                speak("please repeat ,what should i open.")
                continue

            elif 'are you single' in self.cmd:
                speak("No . i am in relationship with wifi")
            elif 'what are you doing' in self.cmd:
                speak("i am currently running your tasks, and listening your dumb questions")
            elif 'do you love me' in self.cmd:
                speak("yeah of course. you are very kind person MRP")
            elif 'i love you' in self.cmd:
                speak('i love you too MRP, but as a programmer')
            elif'feeling not good' in self.cmd:
                speak("you should take a break from daily life")

            elif 'you can sleep' in self.cmd:
                speak("thanks for using. i am always here for you, you can call me anytime.")

                break

            time.sleep(7)
            speak("now what should i do ?")

startexe = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_2.clicked.connect(self.close)

    def start(self):
        # Loading the GIF
        self.movie = QMovie("HD-Side-Flare-Poll-Black-Screen-Design-1080p-Background-.gif")
        self.ui.label.setMovie(self.movie)
        self.startAnimation()
        self.movie = QMovie("animation.gif")
        self.ui.label_2.setMovie(self.movie)
        self.startAnimation()
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startexe.start()

    def showtime(self):
        current_time = QTime.currentTime()
        lable_time = current_time.toString('hh:mm:ss')
        self.ui.textBrowser_2.setText(lable_time)
        self.ui.textBrowser.setText("Radhe... Radhe...")
    def startAnimation(self):
        self.movie.start()




app = QtWidgets.QApplication(sys.argv)
MainWindow = Main()
MainWindow.show()
sys.exit(app.exec())
