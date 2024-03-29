import sqlite3

def insert_values_into_tables(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    try:
        # Insert values
        
        cursor.execute("INSERT INTO Apps_Development (AD_Question, Answer) VALUES (?, ?)", ('True or False: Python is an interpreted language, meaning the code is executed line by line.', 'True'))
        cursor.execute("INSERT INTO Apps_Development (AD_Question, Answer) VALUES (?, ?)", ('Python uses curly braces ({}) to denote code blocks.', 'False'))
        cursor.execute("INSERT INTO Apps_Development (AD_Question, Answer) VALUES (?, ?)", ('True or False: Python is not suitable for building web applications.', 'False'))
        cursor.execute("INSERT INTO Apps_Development (AD_Question, Answer) VALUES (?, ?)", ('True or False: Python uses indentation to define code blocks, such as loops and functions.', 'True'))
        cursor.execute("INSERT INTO Apps_Development (AD_Question, Answer) VALUES (?, ?)", ("True or False: Python's range() function generates a sequence of numbers from a starting value to an ending value.", 'True'))
        
        
        
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