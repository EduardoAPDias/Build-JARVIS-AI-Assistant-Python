import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import os
import pyautogui #pip install pyautogui
import random
import wolframalpha #pip install wolframalpha
import json
import time
from urllib.request import urlopen

engine = pyttsx3.init()
wolframalpha_app_id = 'enter key here'

#for voice in engine.getProperty('voices'): list of voices installed
    #print(voice) print voice information

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0') # setting to this particular voice in en-us
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
    speak("The current time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    
    speak(date)
    speak(month)
    speak(year)
    
def wishme():
    speak("Welcome back Eduardo")
    time_()
    date_()
    
    #Greetings
    
    hour = datetime.datetime.now().hour
    
    if hour>=6 and hour <12:
        speak("Good Mourning Sir!")
    elif hour>=12 and hour <18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("Jarvis at your service. Please tell me how can i help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-US')
        print(query)
            
    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query
    
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #for this function, you must enable low security in the email you are going to use as sender
    
    server.login('username@gmail.ccom','password')
    server.sendmail('username@gmailcom',to,content)
    server.close()
    
def screenshot():
    img = pyautogui.screenshot
    img.save(r'C:\Users\edudi\Pictures\screenshot.png')
    
def cpu():
        usage = str(psutil.cpu_percent())
        speak('CPU is at'+usage)
        battery = psutil.sensors_battery()
        speak('Batery is at')
        speak(battery.percent)
        
def jokes():
        speak(pyjokes.get_joke())
    
if __name__ == "__main__":
        wishme()
        
        while True:
            query = TakeCommand().lower()
            #All commands will be sotore in a lowre case in query
            #for easy recognition
            
            if 'time' in query: #tell us time when asked
                time_() 
            elif 'date' in query: #tell us date when asked
                date_()    
            elif 'wikipedia' in query:
                speak("Searching.....")
                query=query.replace('wikipidia', '')
                result=wikipedia.summary(query,sentences=3)
                speak('According to Wikipedia')
                print(result)
                speak(result)
                
            elif 'send email' in query:
                try:
                    speak("What should i say?")
                    content=TakeCommand()
                    #provide reciever email adress
                    
                    speak("Who is the Reciever")
                    reciever=input("Enter Reciever's Email:")
                    reciever='reciever_is_me@gmail.com'
                    to=reciever
                    sendEmail(to,content)
                    speak(content)
                    speak('Email has been sent.')
                    
                except Exception as e:
                    print(e)
                    speak("Unable to send Email.")

            elif 'search in chrome' in query:
                speak('What should i search')
                chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
                #chromepath is location of chrome's installation on computer
        
                search = TakeCommand().lower()
                wb.get(chromepath).open_new_tab(search+'.com')#only open websites with '.com' at the end
        
            elif 'search youtube' in query:
                speak('What should i search?')
                search_Term = TakeCommand().lower()
                speak("Here we go to Youtube!")
                wb.open('https://www.youtube.com/results?search_query='+search_Term)
            
            elif 'search google' in query:
                speak('What should i search')
                search_Term = TakeCommand().lower()
                speak('Searching...')
                wb.open('https://www.google.com/search?q=' +search_Term)
                
            elif 'cpu' in query:
                cpu()
                
            elif 'joke' in query:
                jokes()
                
            elif 'go offline'in query:
                speak('Going offline sir!')
                quit()
                
            elif 'notepad' in query:
                speak('Opening Note Pad...')
                bloco_notas = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
                os.startfile(bloco_notas)
                
            elif 'write a note'in query:
                speak("What should i write, Sir?")
                notes = TakeCommand()
                file = open('notes.txt','w')
                speak("Sir should I include Date and Time?")
                ans = TakeCommand()
                if 'yes' in ans or 'sure' in ans:
                    strTime = datetime.datetime.now().strftime("%H%M%S")
                    file.write(strTime)
                    file.write(':-')
                    file.write(notes)
                    speak('Done taking notes Sir!')
                else:
                    file.write(notes)
                    
            elif 'show note'in query:
                speak('showing notes')
                file = open('notes.txt','r')
                print(file.read())
                speak(file.read())
                
            elif 'screenshot' in query: 
                screenshot()
                
            elif 'play songs' in query:
                audio = r'C:\Users\edudi\Music'
                video = r'C:\Users\edudi\Videos'
                speak("What should i play? Audio or video?")
                ans = (TakeCommand().lower)
                while (ans != 'audio' and ans != 'video'):
                    speak("I could not understand you.PLease try again...")
                    ans = (TakeCommand().lower())
                    
                if 'audio' in ans:
                    songs_dir = audio
                    songs = os.listdir(songs_dir)
                    print(songs)
                elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    print(songs)
            
                speak("select a random number")
                rand = (TakeCommand().lower())
                while'number' not in rand and rand != 'random':
                    speak("I could not understand you. Please Try again.")
                    rand = (TakeCommand().lower())
                    
                if 'number' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                              
                elif 'random' in rand:
                    rand = random.randint(1,100)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                
            elif 'remember that' in query:
                speak("What should i remember?")
                memory = TakeCommand()
                speak("You asked me to remember that" +memory)
                remember = open('memory.txt','w')
                remember.write(memory)
                remember.close()
                
            elif 'do you remember anything' in query:
                remember = open('memory.txt','r')
                speak('You asked me to remember that'+remember.read())
                
            elif 'where is' in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to locate"+ location)
                wb.open_new_tab("https://www.google.com.br/maps/place/" + location + "")
                
            elif 'news' in query:
                try:
                    jsonObj = urlopen("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=ef34da15c82042b5a35c93eeb4a17900")
                    data = json.load(jsonObj)
                    i = 1
                    
                    speak('Here are some top headlines from Tech Crunch!')
                    print('=====TOP HEADLINES====='+'\n')
                    for item in data['articles']:
                        print(str(i)+'. '+item['title']+'\n')
                        print(item['description']+'\n')
                        speak(item['title'])
                        i += 1
                        
                except Exception as e:
                    print(str(e))
                    
            elif 'calculate' in query:
                client = wolframalpha.Client(wolframalpha_app_id)
                index = query.lower().split().index('calculate')
                query = query.split()[index +1:]
                res = client.query(''.join(query))
                answer = next(res.results).text
                print('The answer is: ' +answer)
                speak('The answer is ' +answer)
                
            elif 'what is' in query or 'who is' in query:
                #use same APi key generated earlier i.e. wolframalpha
                client = wolframalpha.Client(wolframalpha_app_id)
                res = client.query(query)
            
                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No results")
                    
            elif 'stop listening' in query:
                speak('For how many seconds you want me to stop listening to your commands?')
                ans = int(TakeCommand())
                time.sleep(ans)
                print(ans)
                
            elif 'log out' in query:
                os.system("shutdown -1")
            elif 'restart' in query:
                os.system("shutdown /r /t 1")
            elif 'shutdown' in query:
                os.system("shutdown /s /t 1")