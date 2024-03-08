import sqlite3

def insert_values_into_tables(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    try:
        # Insert values
        
        cursor.execute("INSERT INTO Business_Management (BMGT_Question, Answer) VALUES (?, ?)", ("True or False: In Maslow's hierarchy of needs, physiological needs are at the highest level.", 'True'))
        cursor.execute("INSERT INTO Business_Management (BMGT_Question, Answer) VALUES (?, ?)", ('True or False: SWOT analysis stands for Strengths, Weaknesses, Opportunities, and Threats.', 'True'))
        cursor.execute("INSERT INTO Business_Management (BMGT_Question, Answer) VALUES (?, ?)", ('True or False: According to the expectancy theory, employees are motivated when they believe their efforts will lead to desirable performance outcomes.', 'True'))
        cursor.execute("INSERT INTO Business_Management (BMGT_Question, Answer) VALUES (?, ?)", ('True or False: Transformational leadership focuses solely on maintaining the status quo within an organization.', 'False'))
        cursor.execute("INSERT INTO Business_Management (BMGT_Question, Answer) VALUES (?, ?)", ('True or False: The SMART acronym stands for Specific, Measurable, Achievable, Relevant, and Timely.', 'True'))
        
        
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