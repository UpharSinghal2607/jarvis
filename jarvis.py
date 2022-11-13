import sys
import subprocess
import instaloader
import time
import random
import numpy
import numpy as np
import speedtest
import psutil
import gc
from pywikihow import search_wikihow
import pyautogui
from GoogleNews import GoogleNews
import speech_recognition as sr
import winsound
import urllib.request
import pyttsx3
import datetime
import os
import PyPDF2
import pywhatkit
import pygeoip
import wikipedia
import instaloader
import pyjokes
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtCore import QTime,QTimer,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from jarvisUI import Ui_MainWindow
import webbrowser
from googlesearch import search
import requests
import cv2
from bs4 import BeautifulSoup
from urllib.request import urlopen
import smtplib
import playsound
from playsound import playsound
import operator
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)
gc.collect()
def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()



def news():

        main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=950a89b7e110487ca77c53da33308396"
        main_page=requests.get(main_url).json()
        articles = main_page['articles']
        head = []
        day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "nineth", "tenth"]
        for ar in articles:
            head.append(ar['title'])
        for i in range(len(day)):
            talk(f"today's {day[i]} news is {head[i]}")

def pdf_reader():

    book=open('Character Modeling( Swayam) with Maya and ZBrush.pdf','rb')
    pdfReader=PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages
    talk(f"sir total no of pages in this pdf are {pages}")
    talk("sir please tell the page no which i have to read")
    pg=int(input("sir enter the page no.="))
    page=pdfReader.getPage(pg)
    text=page.extractText()
    talk(text)

def email(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()



    server.login('uphar.singhal.tmp@miet.ac.in','9760967976')
    server.sendmail('uphar.singhal.tmp@miet.ac.in',to,content)
    server.close()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        talk("good morning")
    elif hour>12 and hour<18:
        talk("good afternoon")
    else:
        talk("good night")
    talk("hello I am your assistant jarvis how can i help you sir....")
class MainThread(QThread):
    def __init__(self):
         super(MainThread, self).__init__()
    def run(self):
        self.commands()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening....')
            r.pause_threshold = 1
            text = r.listen(source,timeout = 8,phrase_time_limit= 6)

        try:
            print('recognizing....')
            query = r.recognize_google(text,language="en-in")
            print(f"user said: {query}")

        except Exception as e:
            print('please say again.....')
            return "none"
        return query
    def commands(self):
        wish()
        while True:
                self.query=self.takecommand().lower()
                if "what can you do" in self.query:
                    talk("i can do anything you can think")
                    talk("example i can do maths calculations, i can send whatsapp message, i can send email"
                         "and i can play muic or can tell you some joke.....i can open any file as well as application"
                         "i can switch down as well as restart the system for you")
                elif "how are you" in self.query:
                    talk("I am fine sir and what about you")
                elif "bored" in self.query or "sad" in self.query:
                    talk("i can understand sir should i tell you a joke or play some music")


    #########################################################################################################################
    #open notepad
                elif "open notepad" in self.query:
                    npath= "C:\\Windows\\system32\\notepad.exe"
                    os.startfile(npath)

    #########################################################################################################################
    #close notepad
                elif 'close notepad' in self.query:
                    talk("ok sir,closing notepad")
                    os.system("taskkill /f /im notepad.exe")
                elif "open calculator" in self.query:
                    apath= "C:\\Windows\\system32\\calc.exe"
                    os.s(apath)


    ##########################################################################################################################
    #play something on youtube
                elif 'play on youtube'  in  self.query or "youtube" in self.query:
                    talk("what should i play sir")
                    at=self.takecommand().lower()
                    song=at.replace('play...',' ')
                    talk('playing...'+song)
                    pywhatkit.playonyt(song)
    ##########################################################################################################################
    #current time
                elif "time" in self.query:
                    time=datetime.datetime.now().strftime('%H:%M')
                    print(time)
                    talk('current time is ' +time)
    ##########################################################################################################################
    #wikipedia
                elif "find on wikipedia" in self.query or "wikipedia" in self.query:
                    talk("sir what should i search for you")
                    bt=self.takecommand().lower()
                    talk("yes sir wait i am searching")
                    person=bt.replace('find me',' ')
                    info=wikipedia.summary(person,5)
                    print(info)
                    talk(info)
    ##########################################################################################################################
    #google searching
                elif "open google" in self.query:
                    talk("sir,what should I search on google")
                    
                    cm=self.takecommand().lower()
                    talk("yes sir wait i am searching")
                    webbrowser.open(f"{cm}")
    #########################################################################################################################
    #for command prompt
                elif "command prompt" in self.query and "cmd" in self.query:
                    os.system("start cmd")
    ############################################################################################################################
    #for IP Adress
                elif "ip address" in self.query:
                    ip=requests.get('https://api.ipify.org').text
                    talk(f"your ip address is{ip}")
    ##############################################################################################################################
    #send whatsapp message
                elif "message" in self.query:
                    talk("sir,what should I send on whatsapp")
                    dm = takecommand().lower()
                    pywhatkit.sendwhatmsg("+918126979255",f"{dm}",20,14)
    ##########################################################################################################################
    #sending email
                elif "email" in self.query:
                    try:
                        talk("what should I say?")
                        talk("sir please give the content")
                        content=self.takecommand().lower()

                        to="uphar.singhal.tmp@miet.ac.in"
                        email(to,content)
                        talk("email has been sent to"+to)
                    except Exception as e:
                        print(e)
                        talk("sorry sir i am not able to send email ")
    ##########################################################################################################################
    #for jokes
                elif "joke" in self.query:
                    talk(pyjokes.get_joke(language='en',category="neutral"))
                elif "music" in self.query:
                    n=random.randint(0,77)
                    music_dir = "D:\\music"
                    songs = os.listdir((music_dir))
                    os.startfile(os.path.join(music_dir, songs[n]))
    ########################################################################################################################
    #for calculation
                elif "can you calculate" in self.query:


                        r=sr.Recognizer()
                        with sr.Microphone() as source:

                            talk("say, what you want to calculate,example: say 5 plus 5")

                            r.adjust_for_ambient_noise(source)
                            audio=r.listen(source)
                        my_string=r.recognize_google(audio)
                        print(my_string)
                        def get_operator_fn(op):
                            return{
                                '+': operator.add,
                                '-': operator.sub,
                                'x': operator.mul,
                                'divided': operator.truediv,

                            }[op]
                        def eval_binary_expr(op1,oper,op2):
                            op1,op2=int(op1),int(op2)
                            return get_operator_fn(oper)(op1,op2)
                        talk("your result is...")
                        talk(eval_binary_expr(*(my_string.split())))
    #########################################################################################################################
    #to find location using ip address
                elif "where i am" in self.query:
                    gp = requests.get('https://api.ipify.org').text
                    talk(f"your ip address is {gp}")
                    gip=pygeoip.GeoIP("GeoLiteCity.dat")
                    res=gip.record_by_addr(gp)
                    for key,val in res.items():
                        talk('%s : %s' % (key,val))
    #########################################################################################################################
                elif "weather" in self.query:
                    talk("weather of which city do you want to search")
                    search=self.takecommand().lower()
                    url=f"https://www.google.com/search?q={search}"
                    z=requests.get(url)
                    data=BeautifulSoup(z.text,"html.parser")
                    temp=data.find("div",class_="BNeawe").text
                    talk(f"current {search} is {temp}")
    #############################################################################################################################
    #for alarm clock
                elif "alarm" in self.query:
                    talk("at what time do you want to set alarm")
                    time_alarm=input("enter the alarm time=")
                    talk("alarm is set")

                    while True:
                        Time_Ac=datetime.datetime.now()
                        now=Time_Ac.strftime('%H:%M')

                        if now==time_alarm:


                            #talk("Time to wake up sir")

                            music_dir="D:\\music"
                            songs=os.listdir((music_dir))
                            os.startfile(os.path.join(music_dir,songs[0]))



                        elif now>time_alarm:
                            break

    ###########################################################################################################################
    # for shutdown the system
                elif "shutdown the system" in self.query:
                    os.system("shutdown /s /t 5")

    ##########################################################################################################################
    # for restart the system
                elif "restart the system" in self.query:
                    os.system("shutdown /r /t 5")
    ###########################################################################################################################

    # for system to sleep
                elif "system in sleep mode" in self.query:
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    ###########################################################################################################################
    #switching the window
                elif 'switch the window' in self.query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    pyautogui.keyUp("alt")

    #########################################################################################################################
    #for news headlines
                elif "get me some news" in self.query or "news" in self.query:
                    talk("please wait sir ,i am fetching some of the latest news")
                    news()
    ##########################################################################################################################
    #check instagram profiles
                elif "instagram profile" in self.query or "profile on instagram" in self.query:
                    talk("sir please enter the username correctly::")
                    name=input("Enter the usrname::")
                    webbrowser.open(f"www.insagram.com/{name}")
                    talk(f"sir, here is the profile of the user {name}")

                    talk("sir would you like to take the picture of the account")
                    condition=self.takecommand().lower()
                    if "yes" in condition:
                        mod=instaloader.Instaloader()
                        mod.download_profile(name,profile_pic_only=True)
                        talk("done sir i am ready with the download and saved it in main folder")
                    else:
                        pass
    ##########################################################################################################################
    #taking screenshots
                elif "take a screenshot" in self.query or "take screenshot" in self.query:
                    talk("sir tell me the name of the screen shot file")
                    name=self.takecommand().lower()
                    talk("sir hold the screen for few seconds ,till i take the screen shot")
                    img=pyautogui.screenshot()
                    img.save(f"{name}.png")
                    talk("screen shot is ready sir and it saved in main folder ")
    ###########################################################################################################################
    #read pdf
                elif "read pdf" in self.query:
                    pdf_reader()
    ###########################################################################################################################
    #search anything
                elif "search" in self.query:
                    talk("sir please tell me what you want to search")
                    how=self.takecommand()
                    max_result=1
                    how_to=search_wikihow(how,max_result)
                    assert len(how_to)==1
                    how_to[0].print()
                    talk(how_to[0].summary)
    #############################################################################################################################3
    #for battery charging
                elif "power left" in self.query or "battery" in self.query or "power we have" in self.query:
                    battery=psutil.sensors_battery()
                    percentage=battery.percent
                    talk(f"sir our system have {percentage} percent battery")
                    if percentage>=75:
                        talk("sir we have enough power to continue our work")
                    elif percentage>=40 and percentage<=75:
                        talk("sir we should connect our system to charging")
                    elif  percentage>=20 and percentage<=40:
                        talk("sir we don't have enough power please connect to the charger")
                    else:
                        talk("we have very low power ,please connect to charging otherwise will stop working")
    ##########################################################################################################################
    #for mobile camera
                elif "mobile camera" in self.query:
                    url = "https://10.48.240.244:8080"
                    while True:
                        img_arr = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.unit8)
                        img1 = cv2.imdecode(img_arr, -1)
                        cv2.imshow('IPWebcam', img1)
                        q = cv2.waitKey(1)
                        if q == ord("q"):
                            break;
                    cv2.destroyAllWindows()
    #############################################################################################################################
    #for internet speed
                elif "internet speed" in self.query:
                    st=speedtest.Speedtest()
                    dl=st.download()
                    ul=st.upload()
                    talk(f"sir we have {dl} bit per second downloading speed and {ul} bit per second uploading speed")
    ##########################################################################################################################
    #for volume up
                elif "volume up" in self.query:
                    pyautogui.press("volumeup")
    ##########################################################################################################################
    #for mute
                elif "mute" in self.query:
                    pyautogui.press("volumemute")
    ##########################################################################################################################
    #for volume down
                elif "volume down" in self.query:
                    pyautogui.press("volumedown")
    #################################################################################################################################
                elif "goodbye" in self.query:
                    sys.exit()
    ######################################################################################################################################3
                elif "sleep" in self.query:
                    talk("yes sir i am going to sleep you can call me anytime")
                    break
startExecution=MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.starttask)
        self.ui.pushButton_2.clicked.connect(self.close)
    def starttask(self):
        self.ui.movie=QtGui.QMovie("E:\iron.gif")
        self.ui.movie2=QtGui.QMovie("E:\iron2.gif")
        self.ui.jarvis.setMovie(self.ui.movie)
        self.ui.label_2.setMovie(self.ui.movie2)
        self.ui.movie.start()
        self.ui.movie2.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startExecution.start()
    def showtime(self):
        current_time=QTime.currentTime()
        current_date=QDate.currentDate()
        label_time=current_time.toString('hh:mm:ss')
        label_date=current_date.toString(Qt.ISODate)
        self.ui.label_3.setText(label_date)
        self.ui.label_4.setText(label_time)

app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())

