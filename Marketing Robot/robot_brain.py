def process_question(user_text):
    college_map = {
        "library": "on the first floor, next to the main entrance",
        "cafeteria": "on the ground floor, at the end of the hall",
        "lab 1": "on the second floor, room 204",
        "dean's office": "on the third floor, room 301"
    }
    
    text_to_search = user_text.lower()
    
    for keyword, location in college_map.items():
        if keyword in text_to_search:
            return f"The {keyword} is located {location}."
        
    return "I am sorry, I do not have that location in my database yet."

if __name__ == "__main__":
    test_question = "Can you tell me where the lab 1 is?"
    
    print(f"Question: {test_question}")
    answer = process_question(test_question)
    print(f"Robot says: {answer}")