from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3, datetime, sys, wikipedia, wolframalpha, os,urllib, smtplib, random, webbrowser, pygame, subprocess, calendar

# client = wolframalpha.Client('Your_App_ID')

# folder = 'C:\\Users\\skt\\Music\\YouTube\\'

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# b_music = ['Edison', 'Micro', 'Lucid_Dreamer']
# pygame.mixer.init()
# pygame.mixer.music.load(folder + random.choice(b_music) + '.mp3')
# pygame.mixer.music.set_volume(0.05)
# pygame.mixer.music.play(-1)



def speak(audio):
    print('Habilis:', audio)
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def greetings():
    greet = []
    with open("greetings.txt") as file:
        for g in file:
            g = g.strip()
            greet.append(g)
    return (random.choice(greet))

def sendEmail(to,content):
    file = open('password.txt', 'r+')
    passwrd = file.read()
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('azaanzaki7@gmail.com',passwrd)
    server.sendmail('azaanzaki7@gmail.com',to,content)
    server.close()


def takecomm():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Try again')
        pass

    return query


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')

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


class Widget:
    def __init__(self):
        root = Tk()
        root.title('HABILIS')
        root.config(background='dark turquoise')
        root.geometry('350x600')
        root.resizable(0, 0)
        root.iconbitmap(r'E:\azaan\images.jpg')
        img = ImageTk.PhotoImage(Image.open(r"E:\azaan\habilis.jpg"))
        panel = Label(root, image=img)
        panel.pack(side="bottom", fill="both", expand="no")

        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('Click \'Start Listening\' to Give commands')

        userFrame = LabelFrame(root, text="USER", font=('Arial', 10, 'bold'))
        userFrame.pack(fill="both", expand="yes")

        left2 = Message(userFrame, textvariable=self.userText, bg='dark turquoise', fg='black')
        left2.config(font=("Arial", 10, 'bold'))
        left2.pack(fill='both', expand='yes')

        compFrame = LabelFrame(root, text="KAREN", font=('Arial', 10, 'bold'))
        compFrame.pack(fill="both", expand="yes")

        left1 = Message(compFrame, textvariable=self.compText, bg='dark turquoise', fg='black')
        left1.config(font=("Arial", 10, 'bold'))
        left1.pack(fill='both', expand='yes')

        btn = Button(root, text='Start Listening!', font=('Arial', 10, 'bold'), bg='deepSkyBlue2', fg='white',
                     command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close!', font=('Arial', 10, 'bold'), bg='orangered', fg='white',
                      command=root.destroy).pack(fill='x', expand='no')

        speak('Hello, I am Habilis! What should I do for You?')
        self.compText.set('Hello, I am Habilis! What should I do for You?')

        root.bind("<Return>", self.clicked)  # handle the enter key event of your keyboard
        root.mainloop()

    def clicked(self):
        print('Working')
        query = takecomm()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        if 'male voice' in query:
            self.compText.set('okay')
            engine.setProperty('voice', voices[0].id)
            speak('done..')

        elif 'wikipedia' in query:
                self.userText.set(query)
                speak('Searching Wikipedia...')
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query, sentences=2)
                speak('according to wikipedia')
                self.compText.set(results)
                # print(results)
                speak(results)

        elif 'date' in query:
            speak(date())
            self.compText.set(date())


        elif 'search' in query:
            self.compText.set('searching...')
            speak('searching...')
            query = query.replace('search google', '')
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(
                'google.com/search?q=' + ''.join(query))

        elif 'open google' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('google.com')

        elif 'shutdown' in query:
            self.compText.set('okay')
            speak('okay')
            sys.exit()

        elif 'ms word' in query:
            self.compText.set('opening microsoft word')
            speak('opening word....')
            wordpath = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\WINWORD.exe"
            os.startfile(wordpath)

        elif 'email' in query:
            try:
                speak('what should i send ?')
                content = takecomm()
                speak('noted sir...')
                self.userText.set(content)
                # print(content)
                speak('whom to send ?')
                to = takecomm().lower()
                self.userText.set(to)
                # print(to)
                sendto = [sub[to] for sub in emailid]
                sendEmail(sendto[0], content)
                self.compText.set('email sent')
                speak('sent....')
            except Exception as e:
                print(e)
                self.compText.set('sorry')
                speak('sorry')

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            self.compText.set('Okay')
            speak('okay')
            self.compText.set('Bye, have a good day.')
            speak('Bye, have a good day.')

        elif 'hello' in query:
            self.compText.set(greetings())
            speak(greetings())

        elif 'play' in query:
            self.compText.set('playing on youtube')
            speak('playing on youtube...')
            query=query.replace('youtube','')
            print(query)
            qs = urllib.parse.urlencode({"search_query": query})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + qs)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("http://www.youtube.com/watch?v=" + search_results[0])

        else:
            try:
                speak('I don\'t know, I can open something more smarter than me!')
                self.compText.set('I don\'t know, I can open something more smarter than me!')
                webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('google.com')
                # try:
                #     res = client.query(query)
                #     results = next(res.results).text
                #     self.compText.set(results)
                #     speak(results)
                # except:
                #     results = wikipedia.summary(query, sentences=2)
                #     self.compText.set(results)
                #     speak(results)

            except:
                speak('I don\'t know, I can open something more smarter than me!')
                self.compText.set('I don\'t know, I can open something more smarter than me!')
                webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('google.com')


if __name__ == '__main__':
    greetMe()
    widget = Widget()