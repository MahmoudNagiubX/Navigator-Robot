import pyttsx3

def speak_answer(text):
    engine = pyttsx3.init()
    
    rate = engine.getProperty('rate') # Speed
    engine.setProperty('rate', rate - 2000)
    
    print(f"Speaking: '{text}'")
    engine.say(text)
    
    engine.runAndWait()
    
if __name__ == "__main__":
    test_sentence = "Hello! I am your new robot assistant. I am ready to help you find your way around the college."
    speak_answer(test_sentence)