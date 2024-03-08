import sqlite3 as sql
conn=sql.connect('quarterly_assessment.db')
cr=conn.cursor()

# Create Table 1
cr.execute(
    """CREATE TABLE IF NOT EXISTS Finance
    (Finance_Question TEXT PRIMARY KEY, Answer TEXT)""")

# Create Table 2
cr.execute(
    """CREATE TABLE IF NOT EXISTS Analytics
    (Analytics_Question TEXT PRIMARY KEY, Answer TEXT)""")

# Create Table 3
cr.execute(
    """CREATE TABLE IF NOT EXISTS Business_Management
    (BMGT_Question TEXT PRIMARY KEY, Answer TEXT)""")

# Create Table 4
cr.execute(
    """CREATE TABLE IF NOT EXISTS Analytical_Thinking
    (AT_Question TEXT PRIMARY KEY, Answer TEXT)""")

# Create Table 5
cr.execute(
    """CREATE TABLE IF NOT EXISTS Apps_Development
    (AD_Question TEXT PRIMARY KEY, Answer TEXT)""")