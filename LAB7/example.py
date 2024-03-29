import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')

# Create a cursor object
cur = conn.cursor()

# Create a table
cur.execute('''
CREATE TABLE IF NOT EXISTS student_records (
    Student_ID INTEGER PRIMARY KEY,
    Reg_No TEXT,
    Branch TEXT,
    Semester INTEGER,
    Section TEXT,
    CGPA REAL,
    Email TEXT
)
''')

# Insert data
cur.execute('''
INSERT INTO student_records (Reg_No, Branch, Semester, Section, CGPA, Email)
VALUES ('1234', 'CSE', 5, 'A', 8.5, 'student@example.com')
''')

# Commit the changes
conn.commit()

# Query the data
cur.execute('SELECT * FROM student_records')

# Fetch and display the results
records = cur.fetchall()
for record in records:
    print(record)

# Close the connection
conn.close()
