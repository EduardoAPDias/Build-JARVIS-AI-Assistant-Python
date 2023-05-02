import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb

engine = pyttsx3.init()

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