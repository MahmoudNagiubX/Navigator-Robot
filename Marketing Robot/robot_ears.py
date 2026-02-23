import speech_recognition as sr

def listen_to_user():
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("Adjusting for background noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration = 1)
        
            print("Listening... Ask me a question!")
            audio = recognizer.listen(source)
        
            print("Processing your voice...") # Try to recognize the speech using Google's free API
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you repeat?")
        return None
    except sr.RequestError:
        print("Oops! My speech service is down right now.")
        return None
        
if __name__ == "__main__":
    listen_to_user()