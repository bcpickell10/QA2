import sqlite3

def insert_values_into_tables(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    try:
        # Insert values into Table 1
        # Insert values into Table 2
        cursor.execute("INSERT INTO Analytics (Analytics_Question, Answer) VALUES (?, ?)", ('True or False: A p-value measures the strength of evidence against a null hypothesis.', 'True'))
        cursor.execute("INSERT INTO Analytics (Analytics_Question, Answer) VALUES (?, ?)", ('True or False: Outliers always need to be removed from datasets before analysis.', 'False'))
        cursor.execute("INSERT INTO Analytics (Analytics_Question, Answer) VALUES (?, ?)", ('True or False: A histogram is used to represent categorical data.', 'False'))
        cursor.execute("INSERT INTO Analytics (Analytics_Question, Answer) VALUES (?, ?)", ('True or False: Data mining focuses on discovering meaningful patterns and relationships in large datasets.', 'True'))
        cursor.execute("INSERT INTO Analytics (Analytics_Question, Answer) VALUES (?, ?)", ('True or False: Normal distribution has a skewness of zero.', 'True'))
        
        
        
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