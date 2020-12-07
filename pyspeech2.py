import pyttsx3

def SpeakText(command): 
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 

my_text="134"
SpeakText(my_text)
