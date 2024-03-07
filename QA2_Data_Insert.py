import sqlite3

def insert_values_into_tables(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    try:
        # Insert values into Table 1
        cursor.execute("INSERT INTO Finance (Finance_Question, Answer) VALUES (?, ?)", ('True/False: Net income is calculated by subtracting total expenses from total revenues on the balance sheet.', 'False'))
        cursor.execute("INSERT INTO Finance (Finance_Question, Answer) VALUES (?, ?)", ('Operating cash flow excludes cash flows from which of the following activities? a. Financing b. Investing c. Operating d. All of the above', 'd'))
        cursor.execute("INSERT INTO Finance (Finance_Question, Answer) VALUES (?, ?)", ('Operating cash flow represents the cash generated from  normal business ________.', 'operations'))
        cursor.execute("INSERT INTO Finance (Finance_Question, Answer) VALUES (?, ?)", ('Which ratio measures  short-term liquidity? a. Debt-to-equity ratio b. Return on equity c. Current ratio d. Price-earnings ratio', 'c'))
        cursor.execute("INSERT INTO Finance (Finance_Question, Answer) VALUES (?, ?)", ('True/False: A high debt-to-equity ratio indicates a low level of financial risk.', 'False'))
        
        # Insert values into Table 2
        cursor.execute("INSERT INTO Analytics (Analytics_Question, Answer) VALUES (?, ?)", ('True/False: In regression analysis, the dependent variable is the variable being predicted or explained by the independent variable.', 'True'))
        cursor.execute("INSERT INTO Analytics (Analytics_Question, Answer) VALUES (?, ?)", ('In simple linear regression, the equation of the regression line is represented as Y = a + βX + ε, where a is the ________ and β is the regression coefficient.', 'intercept'))
        cursor.execute("INSERT INTO Analytics (Analytics_Question, Answer) VALUES (?, ?)", ('True/False: A p-value less than the significance level indicates that the null hypothesis should be rejected.', 'True'))
        cursor.execute("INSERT INTO Analytics (Analytics_Question, Answer) VALUES (?, ?)", ('The regression coefficient represents the ________ in the dependent variable for a one-unit change in the independent variable.', 'change'))
        cursor.execute("INSERT INTO Analytics (Analytics_Question, Answer) VALUES (?, ?)", (' If the regression coefficient of a variable is negative, what does it indicate? a. There is no relationship between the variables b. An increase in the independent variable is associated with a decrease in the dependent variable c. An increase in the independent variable is associated with an increase in the dependent variable d. The coefficient is not interpretable', 'c'))
        
       
        
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
