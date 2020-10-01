import urllib.parse
import webbrowser
import json
import random
import pyttsx3
import email
import pyspeedtest
import urllib.request
import wikipedia
import speech_recognition as sr
import time
import wolframalpha
import subprocess
import calendar
import datetime
import os
import geocoder
import sys
import psutil
import platform
import smtplib
import requests
import winshell
from urllib.request import urlopen
from playsound import playsound
from configparser import ConfigParser

parser = ConfigParser()
parser.read('modules/config.ini')
gmail_address = (parser.get('USER', 'gmail_address'))
gmail_password = (parser.get('USER', 'gmail_password'))
yourname = (parser.get('USER', 'name'))

assistant = "Friday"

g = geocoder.ip('me')

client = wolframalpha.Client('QAPJPH-92U3EK5UV9')


engine = pyttsx3.init()
engine.setProperty("rate", 173)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)
        query = ''
        

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f'You said: {query}\n')

    except Exception as e:
        return ''
    
    return query.lower()


def takeCommand1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        time.sleep(0.5)
        playsound("sounds\on.wav")
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)
        time.sleep(0.5)
        playsound("sounds\off.wav")
        query = ''
        

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f'You said: {query}\n')

    except Exception as e:

        print('I dont understand...')
        speak("Please say that again")
        return ''
        query = takeCommand1()

    return query.lower()


    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        return("Good Morning sir")
    elif hour >= 12 and hour < 16:
        return("Good Afternoon sir")
    else:
        return('Good Evening sir')


def connect(host = "https://www.google.com"):
            try:
                urllib.request.urlopen(host)
                return True
            except:
                return False

print("Connected" if connect() else "Sorry. You are not connected to the internet at the moment. Please try again later.")
speak(wishMe() if connect() else "Sorry. You are not connected to the internet at the moment. Please try again later.")
    
    
def speak_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=b222a2c747654ac58b07a187c90b217d'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Retrieving latest news from Times Of India')
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        print(articles['title'])
        speak(articles['title'])
        if index == len(arts)-1:
            break
        speak('')
    speak('These were the top headlines, Have a nice day Sir..')


def internetspeed():
    test = pyspeedtest.SpeedTest("www.google.com")
    
        

if __name__ == '__main__':
    print("")
    
wakeword = "friday"

while True:
    text = takeCommand()

    if text.count(wakeword) > 0:
        wishMe = ["Yes Sir", "How may I help you?", "What should I do Sir?", "How can I be of service?"]
        greet = random.choice(wishMe)
        print(greet)
        speak(greet)
        query = takeCommand1().lower()

    
        if 'search wikipedia for' in query:
            speak('Searching Wikipedia....')
            query = query.replace('search wikipedia for', '')
            results = wikipedia.summary(query, sentences=2)
            print('According to Wikipedia')
            speak('According to Wikipedia')
            print(results)
            speak(results)


        if 'search wikipedia about' in query:
            speak('Searching Wikipedia....')
            query = query.replace('search wikipedia about', '')
            results = wikipedia.summary(query, sentences=2)
            print('According to Wikipedia')
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            print("Recycle Bin has been emptied")
            speak("Recycle Bin has been emptied")

        elif 'empty my recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            print("Recycle Bin has been emptied")
            speak("Recycle Bin has been emptied")

        elif 'unread email'in query:
            os.startfile("modules\gmail_module_fetch.py")

        elif "read my emails" in query:
            os.startfile("modules\gmail_module_fetch.py")

        elif "do I have any unread emails" in query:
            os.startfile("modules\gmail_module_fetch.py")

        elif 'camera' in query:
             os.startfile("modules\capture.py")
             print("Please adjust your camera and press SPACEBAR to take picture")
             speak("please adjust your camera and press spacebar to take picture")
             print("Press ESCAPE button to quit")
             speak("Press ESCAPE button to quit")

        elif 'take a photo' in query:
             os.startfile("modules\capture.py")
             print("Please adjust your camera and press SPACEBAR to take picture")
             speak("please adjust your camera and press spacebar to take picture")
             print("Press ESCAPE button to quit")
             speak("Press ESCAPE button to quit")

        elif 'take a picture' in query:
             os.startfile("modules\capture.py")
             print("Please adjust your camera and press SPACEBAR to take picture")
             speak("please adjust your camera and press spacebar to take picture")
             print("Press ESCAPE button to quit")
             speak("Press ESCAPE button to quit")

        elif 'how do i look' in query or 'i look' in query:
             os.startfile("modules\capture.py")
             print("Please adjust your camera and press SPACEBAR to take picture")
             speak("please adjust your camera and press spacebar to take picture")
             print("Press ESCAPE button to quit")
             speak("Press ESCAPE button to quit")


             
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open('https://youtube.com')

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open('https://google.com')

        elif 'open facebook' in query:
            speak("Opening Facebook")
            webbrowser.open('https://www.facebook.com')

        elif 'open instagram' in query:
            speak("Opening Instagram")
            webbrowser.open('https://www.instagram.com')

        elif 'open gmail' in query:
            speak("Opening Gmail")
            webbrowser.open("https://www.gmail.com")

        elif 'what is my name' in query:
            speak("Your name is" + yourname)

        elif 'my name' in query:
            speak("Your name is" + yourname)

        elif ' your name' in query:
            speak("My name is" + assistant)

        elif 'what is your name' in query:
            speak("My name is" + assistant)

        elif 'can I change your name' in query:
            speak("Sorry. You can't change my name at the moment")

        elif 'change your name' in query:
            speak("Sorry. You can't change my name")

            
        elif 'weather' in query:
            api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" +\
                str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

            data = requests.get(api_url)
            data_json = data.json()
            if data_json['cod'] == 200:
                main = data_json['main']
                wind = data_json['wind']
                weather_desc = data_json['weather'][0]
                print('Your Current location is ' + data_json['name'] + data_json['sys']['country'])
                speak('Your Current location is ' + data_json['name'] + data_json['sys']['country'])
                print('Wind speed is ' + str(wind['speed']) + ' metre per second')
                speak('Wind speed is ' + str(wind['speed']) + ' metre per second')
                print('Temperature is ' + str(main['temp']) + 'degree celcius')
                speak('Temperature is ' + str(main['temp']) + 'degree celcius')
                print('Humidity is ' + str(main['humidity']))
                speak('Humidity is ' + str(main['humidity']))


            
        elif 'open microsoft edge' in query:
            speak("Opening Microsoft Edge")
            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge")

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            search=takeCommand1()
            url = 'https://www.youtube.com/results?search_query=' + search
            webbrowser.open(url)
            
        elif 'day is it' in query:
            now = datetime.datetime.now()
            my_date = datetime.datetime.today()
            weekday = calendar.day_name[my_date.weekday()]
            monthNum = now.month
            dayNum = now.day
            month_names = ['January', 'February', 'March', 'April', 'May','June', 'July', 'August', 'September', 'October', 'November','December']
            ordinalNumbers = ['1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12','13', '14', '15', '16', '17','18', '19', '20', '21', '22','23', '24', '25', '26', '27', '28', '29', '30', '31']
            speak('Today is ' + weekday + ' ' + month_names[monthNum - 1] + ordinalNumbers[dayNum - 1] )


        elif 'time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f'Sir, the time is {strTime}')
            speak(f'Sir, the time is {strTime}')

        elif 'time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f'Sir, the time is {strTime}')
            speak(f'Sir, the time is {strTime}')

        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f'Sir, the time is {strTime}')
            speak(f'Sir, the time is {strTime}')

        elif 'google for' in query:
            query = query.replace('google for', '')
            url = 'https://google.com/search?q=' + query
            webbrowser.open(url)
            speak('Here is What I found for' + query)
           

        elif 'joke' in query:
            beforejoke = ["Prepare to Chuckle. Or Groan", "Here you go", "Alright", "I'll let you decide whether this one is sarcastic:"]
            joke = random.choice(beforejoke)
            print(joke)
            speak(joke)
            with open("modules\Jokes.txt") as f:
                lines = f.readlines()
                jokemain = random.choice(lines)
                print(jokemain)
                speak(jokemain)
            
        elif 'news' in query:
            speak_news()

        elif 'headlines' in query:
            speak_news()
            
        elif 'go to sleep' in query:
            sys.exit()

        elif 'sleep' in query:
            sys.exit()

        elif 'google about' in query:
            query = query.replace('google about', '')
            url = 'https://google.com/search?q=' + query
            webbrowser.open(url)
            speak('Here is What I found for' + query)
            

        elif 'send an email'in query:
            try:
                speak("Sir please enter reciever's email id")
                print("Sir please enter reciever's email id")
                recieveremail= input()
                speak('Please type the subject of your email')
                print('Please type the subject of your email')
                subject = input()
                speak('please type the message')
                print('please type the message')
                message = input()
                content = 'Subject: {}\n\n{}'.format(subject, message)
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login(gmail_address, gmail_password)
                mail.sendmail('joelalbertk1@gmail.com', recieveremail, content)
                mail.close()
                speak('Your Email has been sent succesfully ')

            except Exception as e:
                speak("Sorry. I am not authorised to work with your email. This may happen if your given gmail credentials are wrong. Please correct them from the configuration file")
                os.startfile("config.ini")


        elif 'temperature' in query:
            api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" +\
                str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

            data = requests.get(api_url)
            data_json = data.json()
            if data_json['cod'] == 200:
                main = data_json['main']
                wind = data_json['wind']
                weather_desc = data_json['weather'][0]
                print('Your Current location is ' + data_json['name'] + data_json['sys']['country'])
                speak('Your Current location is ' + data_json['name'] + data_json['sys']['country'])
                print('Wind speed is ' + str(wind['speed']) + ' metre per second')
                speak('Wind speed is ' + str(wind['speed']) + ' metre per second')
                print('Temperature is ' + str(main['temp']) + 'degree celcius')
                speak('Temperature is ' + str(main['temp']) + 'degree celcius')
                print('Humidity is ' + str(main['humidity']))
                speak('Humidity is ' + str(main['humidity']))
                

        elif 'fact' in query:
            fact = ["Will do", "Absolutely", "Sure thing", "Here's one", "Of Course"]
            main = random.choice(fact)
            print(main)
            speak(main)
            with open("modules\Facts.txt") as f:
                lines = f.readlines()
                factmain = random.choice(lines)
                print(factmain)
                speak(factmain)

        elif 'fun' in query:
            fact = ["Will do", "Absolutely", "Sure thing", "Here's one", "Of Course"]
            main = random.choice(fact)
            print(main)
            speak(main)
            with open("modules\Facts.txt") as f:
                lines = f.readlines()
                factmain = random.choice(lines)
                print(factmain)
                speak(factmain)
        
            elif 'timer' in query or 'stopwatch' in query:

                speak("For how many minutes?")
                waiting_time = takeCommand()
                waiting_time = waiting_time.replace('minutes', '')
                waiting_time = waiting_time.replace('minute', '')
                waiting_time = waiting_time.replace('for', '')
                waiting_time = float(waiting_time)
                waiting_time = waiting_time * 60
                speak(f'I will remind you in {waiting_time} seconds')

                time.sleep(waiting_time)
                speak('Your time has been finished sir')
        
        elif 'laugh' in query:
            beforejoke = ["Prepare to Chuckle. Or Groan", "Here you go", "Alright", "I'll let you decide whether this one is sarcastic:"]
            joke = random.choice(beforejoke)
            print(joke)
            speak(joke)
            with open("modules\Jokes.txt") as f:
                lines = f.readlines()
                jokemain = random.choice(lines)
                print(jokemain)
                speak(jokemain)

        elif 'riddle' in query:
            riddle = ["Will do", "Absolutely", "Sure thing", "Here's one", "Of Course"]
            main = random.choice(riddle)
            print(main)
            speak(main)
            with open("modules\Riddle.txt") as f:
                lines = f.readlines()
                riddlemain = random.choice(lines)
                print(riddlemain)
                speak(riddlemain)
    

        elif 'random number' in query:
            number = random.randint(0,1000)
            print(number)
            speak(number)

        elif 'toss' in query:
            coin = ["Heads", "Tails"]
            main = random.choice(coin)
            print("It landed on" + main)
            speak(f'It landed on {main}')
            

        elif 'email' in query:
            try:
                speak("Sir please enter reciever's email id")
                print("Sir please enter reciever's email id")
                recieveremail= input()
                speak('Please type the subject of your email')
                print('Please type the subject of your email')
                subject = input()
                speak('please type the message')
                print('please type the message')
                message = input()
                content = 'Subject: {}\n\n{}'.format(subject, message)
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login(gmail_address, gmail_password)
                mail.sendmail('joelalbertk1@gmail.com', recieveremail, content)
                mail.close()
                speak('Your Email has been sent succesfully')

            except Exception as e:
                speak("Sorry. I am not authorised to work with your email. This may happen if your given gmail credentials are wrong. Please correct them from the configuration file")
                os.startfile("config.ini")

        elif "today's date" in query:
            now = datetime.datetime.now()
            my_date = datetime.datetime.today()
            weekday = calendar.day_name[my_date.weekday()]
            monthNum = now.month
            dayNum = now.day
            month_names = ['January', 'February', 'March', 'April', 'May','June', 'July', 'August', 'September', 'October', 'November','December']
            ordinalNumbers = ['1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12','13', '14', '15', '16', '17','18', '19', '20', '21', '22','23', '24', '25', '26', '27', '28', '29', '30', '31']
            speak('Today is ' + weekday + ' ' + month_names[monthNum - 1] + ordinalNumbers[dayNum - 1] )


        elif "write a note" in query: 
            speak("What should i write sir") 
            note = takeCommand1() 
            file = open('F.R.I.D.A.Y.txt', 'w') 
            speak("Sir, Should i include date and time") 
            query = takeCommand1() 
            if 'yes' in query or 'sure' in query: 
                strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note)

        elif "take a note" in query: 
            speak("What should i write sir") 
            note = takeCommand1() 
            file = open('F.R.I.D.A.Y.txt', 'w') 
            speak("Sir, Should i include date and time") 
            query = takeCommand1() 
            if 'yes' in query or 'sure' in query: 
                strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note)

        elif "make a note" in query: 
            speak("What should i write sir") 
            note = takeCommand1() 
            file = open('F.R.I.D.A.Y.txt', 'w') 
            speak("Sir, Should i include date and time") 
            query = takeCommand1() 
            if 'yes' in query or 'sure' in query: 
                strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note)
 
          
        elif "show notes" in query: 
            speak("Showing Notes") 
            file = open("F.R.I.D.A.Y.txt", "r")  
            print(file.read()) 
            speak(file.read(6))

        elif "show my notes" in query: 
            speak("Showing Notes") 
            file = open("F.R.I.D.A.Y.txt", "r")  
            print(file.read()) 
            speak(file.read(6))

        elif "read notes" in query: 
            speak("Showing Notes") 
            file = open("F.R.I.D.A.Y.txt", "r")  
            print(file.read()) 
            speak(file.read(6))

        elif "read my notes" in query: 
            speak("Showing Notes") 
            file = open("F.R.I.D.A.Y.txt", "r")  
            print(file.read()) 
            speak(file.read(6))

        elif "will you be my gf" in query or "will you be my bf" in query:
            willyou = ["I hear that a big part of going out together is deciding where to eat. I'd let you pick all the time", "If you are asking if I'm committed, the answer is 'absolutely", "I love spending time with you. We have a great person-to-virtual-assistant kind of relationship", "I am all for setting dates and chatting with you!"]
            bforgf = random.choice(willyou)
            print(bforgf)
            speak(bforgf)

        
        elif 'system status' in query:
            os, name, version, _, _, _ = platform.uname()
            version = version.split('-')[0]
            cores = psutil.cpu_count()
            cpu_percent = psutil.cpu_percent()
            memory_percent = psutil.virtual_memory()[2]
            disk_percent = psutil.disk_usage('/')[3]
            boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
            running_since = boot_time.strftime("%A %d. %B %Y")
            print("I am currently running on %s version %s.  " % (os, version))
            speak("I am currently running on %s version %s.  " % (os, version))
            print( "This system is named %s and has %s CPU cores.  " % (name, cores))
            speak( "This system is named %s and has %s CPU cores.  " % (name, cores))
            print( "Your current disk usage is %s percent.  " % disk_percent)
            speak( "Your current disk usage is %s percent.  " % disk_percent)
            print( "Current CPU utilization is %s percent.  " % cpu_percent)
            speak( "Current CPU utilization is %s percent.  " % cpu_percent)
            print("Mmemory utilization at %s percent. " % memory_percent)
            speak("Memory utilization at %s percent. " % memory_percent)
            print( "I have been active since %s." % running_since)
            speak( "It's running since %s." % running_since)

        elif 'cpu status' in query or 'cpu usage' in query:
            cpu_percent = psutil.cpu_percent()
            print( "Current CPU utilization is %s percent.  " % cpu_percent)
            speak( "Current CPU utilization is %s percent.  " % cpu_percent)

        elif 'ram usage' in query or 'ram status' in query:
            memory_percent = psutil.virtual_memory()[2]
            print("Current memory utilization is %s percent. " % memory_percent)
            speak("Current memory utilization is %s percent. " % memory_percent)


        else:
            query = query
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    replies = ['alright', 'got it', 'here you go'] 
                    speak(random.choice(replies))
                    print(results)
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('According to wikipedia')
                    print(results)
                    speak(results)
        
            except:
                speak(f'Searching the web for {query}')
                url = 'https://google.com/search?q=' + query
                webbrowser.open(url)

