import sqlite3 as sql
conn=sql.connect('quarterly_assessment.db')
cr=conn.cursor()

cr.execute(
    """CREATE TABLE IF NOT EXISTS Finance
    (Finance_Question TEXT PRIMARY KEY, Answer TEXT)""")

cr.execute(
    """CREATE TABLE IF NOT EXISTS Analytics
    (Analytics_Question TEXT PRIMARY KEY, Answer TEXT)""")

cr.execute(
    """CREATE TABLE IF NOT EXISTS Business_Management
    (BMGT_Question TEXT PRIMARY KEY, Answer TEXT)""")

cr.execute(
    """CREATE TABLE IF NOT EXISTS Analytical_Thinking
    (AT_Question TEXT PRIMARY KEY, Answer TEXT)""")

cr.execute(
    """CREATE TABLE IF NOT EXISTS Apps_Development
    (AD_Question TEXT PRIMARY KEY, Answer TEXT)""")