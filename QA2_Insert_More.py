import sqlite3

def insert_values_into_tables(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    try:
        # Insert values
        
        cursor.execute("INSERT INTO Analytical_Thinking (AT_Question, Answer) VALUES (?, ?)", ('True or False: Analytical thinking involves the ability to break down complex problems into parts.', 'True'))
        cursor.execute("INSERT INTO Analytical_Thinking (AT_Question, Answer) VALUES (?, ?)", ('True or False: Analytical thinking is primarily focused on finding one correct solution to a problem.', 'False'))
        cursor.execute("INSERT INTO Analytical_Thinking (AT_Question, Answer) VALUES (?, ?)", ('True or False: Data analysis is a crucial component of analytical thinking in business.', 'True'))
        cursor.execute("INSERT INTO Analytical_Thinking (AT_Question, Answer) VALUES (?, ?)", ('True or False: Analytical thinking skills are not useful in decision-making processes.', 'False'))
        cursor.execute("INSERT INTO Analytical_Thinking (AT_Question, Answer) VALUES (?, ?)", ('True or False: Critical thinking and analytical thinking are synonymous terms.', 'False'))
        
        
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