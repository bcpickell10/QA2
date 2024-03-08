import sqlite3

def insert_values_into_tables(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    try:
        # Insert values into Table 1
        cursor.execute("INSERT INTO Finance (Finance_Question, Answer) VALUES (?, ?)", ('True or False: The Sharpe ratio measures the excess return per unit of standard deviation of an investment or a trading strategy.', 'True'))
        cursor.execute("INSERT INTO Finance (Finance_Question, Answer) VALUES (?, ?)", ('True or False: A higher Sharpe ratio indicates better risk-adjusted performance.', ''))
        cursor.execute("INSERT INTO Finance (Finance_Question, Answer) VALUES (?, ?)", ('True or False: The debt-to-equity ratio measures financial leverage by dividing its total liabilities by its shareholders equity.', 'True'))
        cursor.execute("INSERT INTO Finance (Finance_Question, Answer) VALUES (?, ?)", ('True or False: Return on Equity (ROE) is calculated by dividing net income by total assets.', 'False'))
        cursor.execute("INSERT INTO Finance (Finance_Question, Answer) VALUES (?, ?)", ('True or False: Gross Profit Margin is calculated by dividing gross profit by total revenue and multiplying by 100 to express it as a percentage.', 'True'))
        
        
        
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