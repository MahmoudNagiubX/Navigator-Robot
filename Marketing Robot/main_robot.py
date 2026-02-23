import speech_recognition as sr
import pyttsx3

# Phase 3: The Mouth (Setup)
def speak(text):
    engine = pyttsx3.init()
    
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 20)
    
    print(f"🤖Robot says: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
# Phase 2: The Brain & Database
def process_question(user_text):
    college_map = {
        "library": "on the first floor, next to the main entrance",
        "cafeteria": "on the ground floor, at the end of the hall",
        "lab 1": "on the second floor, room 204",
        "dean": "on the third floor, room 301"
    }
    
    for room, location in college_map.items():
        if room in user_text:
            return f"The {room} is {location}."
            
    return "I am sorry, I do not have that location in my database yet."

# Phase 1: The Ears (Listening Loop)
def run_robot():
    recognizer = sr.Recognizer()
    
    speak("Hello! I am online and ready to help you navigate the college building.")
    
    with sr.Microphone() as source:
        # Adjust for noise just once at the beginning
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration = 1)
        
        # The Infinite Loop: Keep listening until we say "stop"
        while True:
            print("\n🎤 Listening... (Say 'stop' to exit)")
            
            try:
                audio = recognizer.listen(source, timeout = 5, phrase_time_limit = 5)
                text = recognizer.recognize_google(audio).lower()
                print(f"🗣️ You said: {text}")
                
                # Check if we want to turn the robot off
                if "stop" in text or "exit" in text:
                    speak("Goodbye! Have a great day.")
                    break
                
                # Send the text to the brain, then speak the answer!
                answer = process_question(text)
                speak(answer)
                
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                print("🤷‍♂️ I couldn't understand the audio. Try again!")

if __name__ == "__main__":
    run_robot()