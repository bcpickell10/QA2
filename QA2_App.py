import sqlite3
import random

# ANSI escape codes for colored text
RED = '\033[91m'
GREEN = '\033[92m'
END = '\033[0m'

def select_topic(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    try:
        while True:
            # Retrieve the names of all tables (topics) in the database
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            
            # Display the list of topics to the user
            print("Available Topics:")
            for idx, table in enumerate(tables, start=1):
                print(f"{idx}. {table[0]}")
            
            # Prompt the user to select a topic
            topic_idx = int(input("Enter the number of the topic you want to be quizzed on: "))
            
            # Get the selected topic name
            selected_topic = tables[topic_idx - 1][0]
            
            # Start the quiz for the selected topic
            start_quiz(selected_topic, cursor)
            
            # Ask the user if they want to choose another topic
            choice = input("Do you want to choose another topic? (yes/no): ").lower()
            if choice != "yes":
                break
    
    except sqlite3.Error as e:
        print("Error:", e)
    
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

def start_quiz(topic, cursor):
    print(f"\nWelcome to the {topic} Quiz!\n")
    
    # Construct the column name based on the selected topic
    question_column = None
    if topic == "Finance":
        question_column = "Finance_Question"
    elif topic == "Analytics":
        question_column = "Analytics_Question"
    elif topic == "Business_Management":
        question_column = "BMGT_Question"
    elif topic == "Analytical_Thinking":
        question_column = "AT_Question"
    elif topic == "Apps_Development":
        question_column = "AD_Question"
    else:
        print("Invalid topic selected.")
        return
    
    try:
        # Retrieve questions and answers for the selected topic
        cursor.execute(f"SELECT {question_column}, Answer FROM {topic}")
        questions_answers = cursor.fetchall()
        
        # Shuffle the questions
        random.shuffle(questions_answers)
        
        # Initialize score
        score = 0
        
        # Loop through each question and prompt the user for an answer
        for idx, (question, answer) in enumerate(questions_answers, start=1):
            user_answer = input(f"Question {idx}: {question}\nYour Answer: ")
            
            # Check if the user's answer matches the correct answer
            if user_answer.lower() == answer.lower():
                print(GREEN + "Correct!" + END)
                score += 1
            else:
                print(RED + f"Incorrect! The correct answer is: {answer}" + END)
        
        # Display quiz results
        print("\nQuiz Results:")
        print(f"Total Questions: {len(questions_answers)}")
        print(f"Correct Answers: {score}")
        print(f"Incorrect Answers: {len(questions_answers) - score}")
    
    except sqlite3.Error as e:
        print("Error:", e)

# Replace 'database_file_name.db' with the name of your SQL database file
database_file = 'quarterly_assessment.db'
select_topic(database_file)



