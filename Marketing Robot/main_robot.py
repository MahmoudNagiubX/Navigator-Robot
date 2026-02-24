import speech_recognition as sr
import pyttsx3
import json
import os

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
def process_question(user_text):    # Check if the question is off-topic!
    allowed_keywords = [
        # General College & History
        "ecu", "university", "college", "campus", "founded", "created", "mission", "history",
        # Places & Navigation
        "library", "cafeteria", "lab", "room", "floor", "building", "hall", "entrance",
        # People & Leadership
        "dean", "president", "doctor", "prof", "professor", "head", "staff", "assistant",
        # Engineering & Departments
        "engineering", "faculty", "mechatronics", "software", "construction", "building", 
        "energy", "technology", "mct", "set", "cbe", "departments", "programs",
        # Academics & Admissions
        "credit", "hours", "gpa", "system", "practical", "graduation", "admission", "requirements",
        # Financials
        "fees", "cost", "pay", "installment", "money", "price"
    ]
    
    is_on_topic = any(keyword in user_text for keyword in allowed_keywords)
    
    if not is_on_topic:
        return "I am an ECU Engineering assistant. I cannot answer questions outside of college topics."
    
    try:    # Load real Database\
        current_folder = os.path.dirname(os.path.abspath(__file__))
        database_path = os.path.join(current_folder, "ecu_database.json")
        with open(database_path, "r", encoding="utf-8") as file:
            database = json.load(file)
    except FileNotFoundError:
        return "Error: I am sorry, I do not have that in my database yet."
           
    for room, location in database["locations"].items(): # Search for locations
        if room in user_text:   
            return f"The {room} is {location}."
        
    # Search for History/Facts (Basic Keyword matching) 
    if "founded" in user_text or "created" in user_text:
        year = database['university_core']['foundation_year']
        return f"The university was founded in {year}."
    
    if "programs" in user_text or "departments" in user_text:   # Loop through the new departments list to get their names
        departments = database["faculty_of_engineering_and_technology"]["academic_departments"]
        program_names = [dept["department_name"] for dept in departments]
        programs_text = ", ".join(program_names)
        return f"The engineering programs are: {programs_text}."

    return "I am still learning about ECU. I don't have the answer to that specific question yet."

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