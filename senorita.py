import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import cv2
import time

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("The Current time is")
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
     speak("The Current date is")
     year=int(datetime.datetime.now().year)
     month=int(datetime.datetime.now().month)
     day=int(datetime.datetime.now().day)
     speak(day)
     speak(month)
     speak(year)

def wishme():
    speak("Welcome Back Sir!")
        
    
    
    
    time()
    
    date()
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<16:
        speak("Good Afternoon sir")
    elif hour>=16 and hour<=22:
        speak("Good Evening sir")
    else:
        speak("Good Night Sir")
    speak("Senorita at your service , Please tell me how can i help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        print()
        print()
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(query)
        if len(query)==0:
            return takeCommand()
    except Exception as e:
        print(e)
        speak("Say that again Please")
        return takeCommand()
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    email="maddybhat907@gmail.com"
    server.login(email,"")#change your email and password here!!!!
    server.sendmail(email,to,content)
    server.close()
    
        

def screenshot():
    print("Press a key to take screenshot.....")
    speak("Press a key to take screenshot")
    input()
    img=pyautogui.screenshot()
    speak("Enter the name of the screenshot image")
    print("Enter the name of the image file!")
    name=input()
    
    img.save("C:\\Users\\Madhav Bhat K\\Pictures\\Screenshots\\"+name+".png")
    img=cv2.imread("C:\\Users\\Madhav Bhat K\\Pictures\\Screenshots\\"+name+".png")
    speak("Do you want to preview the image?")
    sure=takeCommand()
    if "yes" in sure:
        
        cv2.imshow("Present ScreenShot",img)
        cv2.waitKey(0)

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())
    


if __name__=="__main__":
    wishme()
    Run=True
    while(Run):
        query=takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            
            date()
        elif 'wikipedia' in query:
            speak("Searching")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "email" in query:
            try:
                
                speak("What Should I say?")
                content=takeCommand()
                speak("Enter the gmail address")
                print("Enter the gmail address")
                to=input()
                
                sendemail(to,content)
                speak("Email has been Sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
            
            speak("Press a key to continue")
            print("Press a key to continue....")
            input()
            
        elif "chrome" in query:
            speak("What should i search in Chrome")
            chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
            speak(search +" has been initiated in the browser")
            print("Press any key to continue......")
            input()
        
        elif "restart" in query:
            speak("Are you sure you want to restart  the system?")
            sure=takeCommand()
            if "yes" in sure:
                
                speak("The system is restarting!")
                os.system("shutdown /r /t 1")
            else:
                print("Press any key to continue....")
                speak("Press any key to continue")
                input()
            
        elif "shutdown" in query:
            speak("Are you sure, you want to Shutdown the system?")
            sure=takeCommand()
            if "yes" in sure:
                
            
                speak("The system is Shutdowning!")
                os.system("shutdown /s /t 1")
            else:
                print("Press any key to continue....")
                speak("Press any key to continue")
                input()
            
        elif "logout" in query:
            speak("Are you sure you want logout of the system?")
            sure=takeCommand()
            if "yes" in sure:
                
            
                speak("The system is Logged Out!")
                os.system("shutdown -l")
            else:
                speak("Press a key to Continue")
                print("Press a key to continue....")
                input()
                
        elif "remember" in query:
            speak("What Should I remember?")
            data=takeCommand()
            speak("You said me to remember "+data)
            remember=open("data.txt",'w')
            remember.write(data)
            remember.close()
            speak("Press a key to continue")
            print("Press a key to continue.....")
            input()
        elif "know" in query:
            remember=open("data.txt","r")
            data=remember.read()
            speak("You said to remember me that "+data)
            
            remember.close()
            speak("Do you want Clear the Schedule list? ")
            int1=takeCommand()
            if "yes" in int1:
                file=open("data.txt","r+")
                file.truncate(0)
                file.close()
                speak("The Schedule list has been Cleared")
            speak("Press a key to continue")
            print("Press a key to Continue.......")
            input()
            
                
                
        elif "screenshot" in query:
            screenshot()
            speak("Done! Took Screenshot")
            print("Press a key to continue...")
            speak("Press a key to continue")
            input()
        
        elif "cpu" in query:
            cpu()
            print("Press a key to continue...")
            speak("Press a key to continue")
            input()
        elif "joke" in query:
            jokes()
            speak("Hope you liked the joke!")
            print("Press a key to continue...")
            speak("Press a key to continue")
            input()
        
            
          
        elif "offline" in query:
            
            Run=False
            quit()
        else:
            speak("I did not understand what you were telling!")
            speak("Please try again!!!") 
          
            
            
        

    


