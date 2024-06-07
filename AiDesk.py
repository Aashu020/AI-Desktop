import getpass
import gettext
import smtplib
import pyttsx3
import speech_recognition as sr
import pywhatkit as pwt
import datetime
import wikipedia
import webbrowser
import os

def chat(query):
    if "tell me about yourself" in query:
        speak(" i am jarvis. i am a desktop assistant created by you ")
    
    
    
    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    
    else:speak("Good Evening!")
     
    speak("my name is jarvis . please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language="en-in")
        print("user said",query)

    except Exception as e:
        #print(e)
        print("say that again i dont get you....")
        speak("say that again i dont get you....")
        return "None"
        

    return query



if __name__ == "__main__":
    wishMe()
    while True:
    
    
        query = takeCommand().lower()
    
    
         #logic on executive tasks based on qyery
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query1 = query.replace("wikipedia","")
            results= wikipedia.summary(query1,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif " open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "d:\\music\\fav songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs [0]))

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")

        elif "open code" in query:
            codepath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif "google" in query:
            speak("Googling...")
            c = query
            d=c[7:]
            e=d+" google.com"
            if d is not None:
                webbrowser.open(e)
            else:
                speak("sorry some error occured")
            # speak("Google ")
            # print(result)
            # speak(result1)
            
        elif "send email" in query:
            try:
                speak("what should I say")
                message=takeCommand()
                senderemail="ur@gmail.com" #add sender gmail
                rec_email="receiver@gmail.com" # add receiver gmail
                password="urpassword" # add app password generate it form sender gmail> security> app password> name it jarvis and generate
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(senderemail,password)
                speak("mailed")
                server.sendmail(senderemail,rec_email,message)
                speak("email success")
                
            except Exception as e:
                print(e)
                speak("I am Unable to send the email")
                        
        elif "youtube" in query:
            speak("found related videos on youtube")
            a=query
            # print(a)
            b=a[7:]
            # print(c)
            pwt.playonyt(b)
            # openyt=webbrowser.open(query2)
            
            speak("here")
            


        else:
            chat(query)