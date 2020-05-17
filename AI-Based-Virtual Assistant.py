import pyttsx3
import datetime
import speech_recognition as sr 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<6:
        speak("Good night")
    elif hour>=6 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<4:
        speak("Good afternoon")
    else:
        speak("Good Evening")

    speak("Welcome to Covid virtual assistant")
    
def takeCommand():
    # takes my command from microphone and gives text
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("user said : ", query)
    except Exception as e:
        print(e)
        speak("Sorry Dear, can you repeat that again?")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can i help you?")
        query = takeCommand().lower()
        if query == 'none':
           print('Check Your Internet Connection. If voice is not reconized')
        elif ' andhra pradesh helpline number' in query:
            speak("0866-2410978")
        elif ' arunachal pradesh helpline number' in query:
            speak("9436055743")
        elif ' assam helpline number' in query:
            speak("6913347770")
        elif ' bihar helpline number' in query:
            speak("104")
        elif ' chhattisgarh helpline number' in query:
            speak("104")
        elif ' goa  helpline number' in query:
            speak("104")
        elif ' gujarat helpline number' in query:
            speak("104")
        elif ' haryana helpline number' in query:
            speak("8558893911")
        elif ' himachal pradesh  helpline number' in query:
            speak("104")
        elif ' jharkhand helpline number' in query:
            speak("104")
        elif ' karnataka helpline number' in query:
            speak("104")
        elif ' kerala helpline number' in query:
            speak("0471-2552056")
        elif ' mahrastra helpline number' in query:
            speak("020-26127394")
        elif ' manipur helpline number' in query:
            speak("3852411668")
        elif ' meghalaya helpline number' in query:
            speak("108")
        elif ' mizoram helpline number' in query:
            speak("102")
        elif ' nagaland  helpline number' in query:
            speak("7005539653")
        elif ' odisha helpline number' in query:
            speak("9439994859")
        elif ' punjab helpline number' in query:
            speak("104")
        elif ' rajasthan helpline number' in query:
            speak("0141-2225624")
        elif ' sikkim helpline number' in query:
            speak("104")
        elif ' tamil Nadu  helpline number' in query:
            speak("044-29510500")
        elif ' telangana  helpline number' in query:
            speak("104")
        elif ' tripura helpline number' in query:
            speak("0381-2315879")
        elif ' uttarakhand  helpline number' in query:
            speak("104")
        elif ' uttar Pradesh helpline number' in query:
            speak("18001805145")
        elif ' west bengal helpline number' in query:
            speak("1800313444222")
        elif ' andaman and nicobar helpline number' in query:
            speak("03192-232102")
        elif ' chandigarh  helpline number' in query:
            speak("9779558282")
        elif '  daman & diu  helpline number' in query:
            speak("104")
        elif ' delhi  helpline number' in query:
            speak("011-22307145")
        elif ' jammu & kashmir helpline number' in query:
            speak("01912520982")
        elif ' ladakh  helpline number' in query:
            speak("01982256462")
        elif ' lakshadweep helpline number' in query:
            speak("104")
        elif ' puducherry helpline number' in query:
            speak("104")
        elif ' central helpline number' in query:
            speak("+91-11-23978046")
        elif 'nodal officer of state goverment' in query:
            webbrowser.open("https://mhrd.gov.in/sites/upload_files/mhrd/files/upload_document/List_of_nodal_Officer_-_NMMSS.pdf")
            speak("nodal officer list is opened")
        elif 'how to prevent corona virus' in query:
            webbrowser.open("https://www.mohfw.gov.in/pdf/ProtectivemeasuresEng.pdf")
            speak("Plz read Care fully")
        elif 'corona virus cases in india' in query:
            webbrowser.open("https://www.mohfw.gov.in/")
            speak("All the Information Regarding to Corona Virus")
        elif 'what is corona virus' in query:
            speak("corona viruses are a type of virus.")
        elif 'corona virus medicine' in query:
            speak("There is no coronavirus vaccine yet. Prevention involves frequent hand-washing, coughing into the bend of your elbow, staying home when you are sick and wearing a cloth face covering if you can't practice social distancing.")
        elif 'can the coronavirus disease spread through food' in query:
            speak("Current evidence on other coronavirus strains shows that while coronaviruses appear to be stable at low and freezing temperatures for a certain period, food hygiene and good food safety practices can prevent their transmission through food.")
        elif 'how long does coronavirus stay on surfaces' in query:
            speak("There is currently no data available on stability of 2019-nCoV on surfaces.")
        elif 'what is the recovery time' in query:
            speak(" the median time from onset to clinical recovery for mild cases is approximately 2 weeks and is 3-6 weeks for patients with severe or critical disease.")
        elif 'arogya setu app download' in query:
            webbrowser.open("https://play.google.com/store/apps/details?id=nic.goi.aarogyasetu&hl=en_IN")
            speak("Your Personal Bodyguard")
        elif 'world wide patient of corona virus' in query:
            webbrowser.open("https://www.worldometers.info/coronavirus/#countries")
            speak("world wide corona patient.")
        elif 'How to use Aarogya Setu App' in query:
            webbrowser.open("https://zeenews.india.com/hindi/india/bihar-jharkhand/video/arogya-setu-app-will-protect-against-corona-virus/681404")
            speak("Please Watch Carefully.")
        elif 'live update twitter ' in query:
            webbrowser("https://twitter.com/i/events/1240662046280048646?lang=en")
            speak("Live Update on Twitter.")
        elif ' w h o corona update via instagram' in query:
            webbrowser("https://www.instagram.com/who/?hl=en")
            speak("WHO Updates.")
        elif 'corona testing centre' in query:
            webbrowser("https://www.investindia.gov.in/team-india-blogs/government-approved-testing-centers-covid-19-india")
            speak("All Testing Centers IN India.")
        elif 'what is coronavirus' in query:
            speak("corona viruses are a type of virus.")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open code' in query:
            codepath = "D:\python22\VA.py"
            os.startfile(codepath)
        elif 'hello' in query:
            speak("Hello Dear")
        elif ' what\'s up' in query or 'how are you' in query:
            speak("i am fine")
        elif 'stop' in query or 'nothing' in query or 'abort' in query or 'bye' in query:
            speak("Bye Dear, have a good day")
            speak("stay fit stay home")
            exit()
        else :
            webbrowser.open(query)
      
