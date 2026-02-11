import pyttsx3
import speech_recognition as sr
import webbrowser  
import datetime 
import pyjokes
import time


def speechtotxt():
    recognizer = sr.Recognizer()   #Recognizer class speech_recognition me hota jo sab speech ko appne pass rkhta h
    with sr.Microphone() as source:  
        # hmm microphone se data lene wale h. speech_recognition Micropone ke sath kaam krke uske source ko lene wla h. ye microphone hamari baato ko lene wla h.
        print("listening.........")
        recognizer.adjust_for_ambient_noise(source)  #ye aas-pass ki aawaj ko hatata h.
        audio =recognizer.listen(source)     #ye source se jo bhi data aayega usko listen karega.
        try: #try except se hmm agr bol rhe h to vo print ho rha nhi to data handle ho jayega.
            print("recognizing.....") 
            data = recognizer.recognize_google(audio)    #isse google reconize se audio ko listen kr rha h.
            print(data)                           
            return data                 
        except sr.UnknownValueError:                     
            print("Not Understand...")               

            

def txttospeech(x):                   
    engine = pyttsx3.init()         #pyttsx3 me init class hota h data ko lata h aur funtion lagata h.            
    voices = engine.getProperty('voices')     #engine.getProperty se hmm property ko get krte h.                 
    engine.setProperty('voice',voices[0].id)  #engine.setProperty se hmm property ko set krte h. jaise isme voice ka property ka kr rhe h voice[0] male voice aayega voice[1] se female voice aayega. 
    rate = engine.getProperty('rate')             
    engine.setProperty('rate',110)                      
    engine.say(x)                                         
    engine.runAndWait()
# txttospeech("welcome to vscode nitish babu")

if __name__ == '__main__':  # ye programm ko split kr dega yeha se do 
     
    # if "hey jarvis" in speechtotxt().lower():
        while True :
                data1 = speechtotxt().lower()
                #isse jo bolenge lower  me type hoga 
                
                if "your name" in data1:
                    name = "my name is jarvis"
                    txttospeech(name)
        
                elif "are you" in data1:
                    own = "I am your Assistant Nitish sir"
                    txttospeech(own)
        
                elif "are age" in data1:
                    age = " i am 5 year old sir"
                    txttospeech(age)
                
                # elif 'time' in data1:
                #     time = datatime.datetime.now().strftime("%I%M%P")
                #     txttospeech(time)
                
                elif 'youtube' in data1:
                    webbrowser.open("https://www.youtube.com/")
        
                elif 'google' in data1:
                    webbrowser.open("https://www.google.com/")
        
                elif "joke" in data1:
                    jokes = pyjokes.get_joke(language="en",category="netural")
                    speechtotxt(jokes)
        
                elif "exit" in data1:
                    speechtotxt("thank you")
                    break
                
                time.sleep(5)

else:

    print("thank")







