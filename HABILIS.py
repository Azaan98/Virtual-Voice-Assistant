import pyttsx3
import os
import wikipedia
import webbrowser
import speech_recognition as sr
import requests,sys,bs4
import urllib.request
import urllib.parse
import re
import smtplib
import random
import datetime
import calendar

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

loop=True

emailid = [{'game':'azaanz300798@gmail.com',
           'azan':'villerx@gmail.com'}]

def sendEmail(to,content):
    file = open('password.txt', 'r+')
    passwrd = file.read()
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('azaanzaki7@gmail.com',passwrd)
    server.sendmail('azaanzaki7@gmail.com',to,content)
    server.close()

def greetings():
    greet = []
    with open("greetings.txt") as file:
        for g in file:
            g = g.strip()
            greet.append(g)
    return (random.choice(greet))


# def change():
#     speak('tell me what to write')
#     content = takecomm()
#     print(content)
#     speak('is it ok now ?')
#     query=takecomm()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]  # e.g. Monday
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'February', 'March', 'April', 'May',
                   'June', 'July', 'August', 'September', 'October', 'November',
                   'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th',
                      '7th', '8th', '9th', '10th', '11th', '12th',
                      '13th', '14th', '15th', '16th', '17th',
                      '18th', '19th', '20th', '21st', '22nd',
                      '23rd', '24th', '25th', '26th', '27th',
                      '28th', '29th', '30th', '31st']


    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'

def takecomm():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        # r.non_speaking_duration=1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-US')
        print(f"user said: {query}\n")

    except Exception as e:
        # speak('say that again....')
        return 'None'
    return query

if __name__ == "__main__":
    speak('hello, how may i help you ?')
    while True:
        query = takecomm()
        query=query.lower()

        if 'female voice' in query:
            engine.setProperty('voice', voices[1].id)
            speak('done..')

        elif 'date' in query:
            speak(date())
            print(date())

        elif 'hello' in query:
            greetings()

        elif 'wikipedia' in query:
            if query == 'wikipedia':
                speak('what to search on wikipedia ?')
                query=takecomm()
                results = wikipedia.summary(query, sentences=2)
                speak('according to wikipedia')
                print(results)
                speak(results)
            else:
                speak('Searching Wikipedia...')
                query=query.replace('wikipedia','')
                results = wikipedia.summary(query, sentences=2)
                speak('according to wikipedia')
                print(results)
                speak(results)

        elif 'email' in query:

            try:
                speak('what should i send ?')
                content = takecomm()
                speak('noted sir...')
                print(content)
                speak('whom to send ?')
                to = takecomm().lower()
                print(to)
                sendto = [sub[to] for sub in emailid]
                sendEmail(sendto[0],content)
                speak('sent....')

            except Exception as e:
                print(e)
                speak('sorry')

        elif 'open google' in query:
            speak('opening google...')
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('google.com')

        elif 'search' in query:
            speak('searching...')
            query=query.replace('search google','')
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('google.com/search?q='+''.join(query))

        elif 'play' in query:
            speak('playing on youtube...')
            query=query.replace('youtube','')
            print(query)
            qs = urllib.parse.urlencode({"search_query": query})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + qs)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("http://www.youtube.com/watch?v=" + search_results[0])

        elif 'visual' in query:
            speak('opening visual...')
            vspath = "C:\\Program Files (x86)\\Microsoft Visual Studio 12.0\\Common7\\IDE\\devenv.exe"
            os.startfile(vspath)

        elif 'ms word' in query:
            speak('opening word....')
            wordpath = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\WINWORD.exe"
            os.startfile(wordpath)

        elif 'quit' or 'exit' in query:
            if query == 'quit':
                speak('quitting...')
                sys.exit()
            elif query=='exit':
                speak('exiting...')
                sys.exit()


