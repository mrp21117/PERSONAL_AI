import speech_recognition as sr
import os
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
import sys

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.wakeup()

    def wakeup(self):
        def takecommand(self):
            listener = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                listener.pause_threshold = 1
                audio = listener.listen(source,timeout=1,phrase_time_limit=7)
            try:
                command = listener.recognize_google(audio,language='en-in')
            except Exception as e:
                return "none"
            return command.lower()

        while True:
            wake = wakeup().takecommand().lower()
            if "hello radhe" in wake:
                os.startfile("D:\\PYTHON\\AI Software\\Radhey\\UI\\Radhey.py")
            else:
                print("sleeping...")