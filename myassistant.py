import pyttsx3
import speech_recognition as sr    #for take cammand
import random
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit




engine = pyttsx3.init('sapi5')   #take voices
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)  #for set voice property

def speak(audio):
    engine.say(audio) #engine say audio string
    engine.runAndWait() #runandwait fuction
def wishme():
      hour = int(datetime.datetime.now().hour)
      if hour>=0 and hour<12:
            speak("good morning!")
      elif hour>12 and hour<18:
            speak("good afternoon!")
      else:
            speak("good afternoon!")
      speak("i am kelwin sir. please tell me how i may help you")
def takecommand():
  #it take microphone input from the user and return string output
 r = sr.Recognizer() #thi is help to recognize audio
 with sr.Microphone() as source:
    print("listning....")
    r.pause_threshold = 1     #bolne me ghap le saku 1 sec ka

    audio = r.listen(source)
    
 try:                                #try tb likhte hai jb hamme lagta hai error aa sakta hai
    print("Recognizing...")
    query = r.recognize_google(audio,language='en-in')
    print(f"user said: {query}\n")
 except Exception as e:           #if error then goto bloack exception and print say that again please
    
    print("say that again please...")
    return "None"
 return query
l = ['avanish','+919335198236','arin','+919368452064','papa','+916393347887']
def getNum(l, query):  #two argment list and name
      counter = 0   #list start from 0
      for i in l:
            if i == query:
              numindex = counter +1  #if name match then respective phone number next
              num =l[numindex]
              return num
            counter = counter+1
      return None
if __name__ == '__main__':
      wishme()
      while True:       #sunta rhega continue
        query = takecommand().lower()
        
        
        if 'wikipedia' in query:
              speak('searching wikipedia...')
              query = query.replace("wikipedia","")
              results = wikipedia.summary(query,sentences=3)
              speak("According to wikipedia")
              speak(results)
    
        elif 'open youtube' in query:
              webbrowser.open("youtube.com")
        elif 'open google' in query:
              webbrowser.open("google.com")
       
        elif 'open facebook' in query:
              webbrowser.open("facebook.com")
        elif 'play music' in query:
            music = 'B:\project 3.0\music'
            songs = os.listdir(music)
            print(songs)
            i = random.randint(1,2)
            os.startfile(os.path.join(music,songs[i]))
        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"sir, the time is {strTime}")
        elif 'open code' in query:
              codepath = "C:\\Users\\myada\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
              os.startfile(codepath)
        elif 'open my college' in query:
              webbrowser.open("http://www.nitra.ac.in/")
        elif 'listen' in query:
             speak("yes sir, i am listen carefully")
    
        elif 'send whatsapp message to' in query:
              name = query.replace('send whatsaap message to','')
              name = name.strip()
              number = getNum(l,name)
              engine.say('what you like to me say')
              engine.runAndWait()
              newquery =takecommand() #store in another variable
              engine.say('what time you like to send messege please say')
              engine.runAndWait()
              sendTime = takecommand()
              if ':' in sendTime:    #removing column speace b/w digit and converting to intiger
                    sendTime= sendTime.replace(':','')
                    engine.say('message to '+name+ 'has been scheduled')  #notifie to user massege has been schedule
                    engine.runAandWait()
                    hours = sendTime[0:2]
                    hours = int(hours)
                    minutes = sendTime[3:5]
                    minutes = int(minutes)
                    pywhatkit.sendwhatmsg(number,newquery,hours,minutes)