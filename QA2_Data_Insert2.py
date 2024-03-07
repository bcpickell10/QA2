import sqlite3

def insert_values_into_tables(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    try:
        # Insert values into Table 3
        cursor.execute("INSERT INTO Business_Management (BMGT_Question, Answer) VALUES (?, ?)", ('True/False: Ethical decision making involves considering only the short-term consequences of actions.', 'False'))
        cursor.execute("INSERT INTO Business_Management (BMGT_Question, Answer) VALUES (?, ?)", ('Multiple Choice: Which of the following is NOT a step in the ethical decision-making process? a. Identifying the ethical dilemma b. Evaluating potential consequences c. Ignoring the consequences of actions d. Making a decision and taking action', 'c'))
        cursor.execute("INSERT INTO Business_Management (BMGT_Question, Answer) VALUES (?, ?)", ('True/False: Ethical leaders prioritize personal gains over the well-being of their team and organization.', 'False'))
        cursor.execute("INSERT INTO Business_Management (BMGT_Question, Answer) VALUES (?, ?)", ('Ethical leaders demonstrate ________ by holding themselves and others accountable for their actions.', 'accountability'))
        cursor.execute("INSERT INTO Business_Management (BMGT_Question, Answer) VALUES (?, ?)", ('Upholding core ________ such as honesty and integrity contributes to fostering an ethical workplace culture.', 'values'))
        
        # Insert values into Table 4
        cursor.execute("INSERT INTO Analytical_Thinking (AT_Question, Answer) VALUES (?, ?)", ('True/False: Critical thinking involves accepting information at face value without questioning its validity.', 'False'))
        cursor.execute("INSERT INTO Analytical_Thinking (AT_Question, Answer) VALUES (?, ?)", ('True/False: Professionalism in the workplace includes demonstrating integrity and ethical behavior.', 'True'))
        cursor.execute("INSERT INTO Analytical_Thinking (AT_Question, Answer) VALUES (?, ?)", ('What does professionalism entail in a business setting? a. Dressing formally at all times b. Following ethical guidelines and standards c. Ignoring deadlines and commitments d. Avoiding collaboration with colleagues', 'b'))
        cursor.execute("INSERT INTO Analytical_Thinking (AT_Question, Answer) VALUES (?, ?)", ('Effective problem-solving requires a ________ approach, considering various perspectives and potential solutions.', 'systematic'))
        cursor.execute("INSERT INTO Analytical_Thinking (AT_Question, Answer) VALUES (?, ?)", ('Which of the following is NOT a step in effective problem-solving? a. Identifying the root cause of the problem b. Implementing the first solution that comes to mind c. Evaluating potential solutions d. Monitoring the outcomes of the chosen solution', 'b'))
        
        # Insert values into Table 5
        cursor.execute("INSERT INTO Apps_Development (AD_Question, Answer) VALUES (?, ?)", ('True/False: Python is a compiled programming language, meaning code is translated into machine language before execution.', 'False'))
        cursor.execute("INSERT INTO Apps_Development (AD_Question, Answer) VALUES (?, ?)", ('In Python, a ________ is a collection of items that are ordered and changeable.', 'list'))
        cursor.execute("INSERT INTO Apps_Development (AD_Question, Answer) VALUES (?, ?)", ('In Python, the ________ method is used to execute SQL queries on an SQLite database.', 'execute'))
        cursor.execute("INSERT INTO Apps_Development (AD_Question, Answer) VALUES (?, ?)", ('Which SQL statement is used to retrieve data from a database? a. SELECT b. UPDATE c. DELETE d. INSERT', 'b'))
        cursor.execute("INSERT INTO Apps_Development (AD_Question, Answer) VALUES (?, ?)", ('The ________ statement in SQL is used to add new records to a database table.', 'INSERT'))
        
        # Commit the changes to the database
        conn.commit()
        
        print("Values inserted into tables successfully.")
    
    except sqlite3.Error as e:
        print("Error inserting values into tables:", e)
        
        # Rollback the transaction if an error occurs
        conn.rollback()
    
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

# Replace 'database_file_name.db' with the name of your SQL database file
database_file = 'quarterly_assessment.db'
insert_values_into_tables(database_file)
