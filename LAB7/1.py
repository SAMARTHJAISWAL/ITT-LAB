import sqlite3

conn=sqlite3.connect('Q1.db')
print('opened')

cur=conn.cursor()

cur.execute('''
CREATE TABLE STUDI
(STUDENT_ID INT PRIMARY KEY NOT NULL,
REG_NO TEXT,
BRANCH TEXT,
SEM INT,
SEC TEXT,
CGPA REAL,
EMAIL TEXT
)
''')

print('created')

cur.execute("INSERT INTO STUDI VALUES (101,'2001', 'CSE', 5, 'A', 9.1, 'student1@example.com')")
cur.execute("INSERT INTO STUDI VALUES (102,'2002', 'ECE', 6, 'B', 8.7, 'student2@example.com')")
cur.execute("INSERT INTO STUDI VALUES (103,'2003', 'MECH', 4, 'A', 7.8, 'student3@example.com')")
cur.execute("INSERT INTO STUDI VALUES (104,'2004', 'CIVIL', 7, 'A', 8.9, 'student4@example.com')")
cur.execute("INSERT INTO STUDI VALUES (105,'2005', 'IT', 5, 'B', 9.4, 'student5@example.com')")

print('inserted')

cursor = cur.execute("SELECT * FROM STUDI")
for row in cursor:
    print("STUDENT_ID = ", row[0])
    print("REG_NO = ", row[1])
    print("BRANCH = ", row[2])
    print("SEM = ", row[3])
    print("SEC = ", row[4])
    print("CGPA = ", row[5])
    print("EMAIL = ", row[6], "\n")

print("sorting started")

cursor=cur.execute('SELECT * FROM STUDI ORDER BY CGPA DESC')
for row in cursor:
    print("STUDENT_ID = ", row[0])
    print("REG_NO = ", row[1])
    print("BRANCH = ", row[2])
    print("SEM = ", row[3])
    print("SEC = ", row[4])
    print("CGPA = ", row[5])
    print("EMAIL = ", row[6], "\n")
    
print("sorting done")
conn.close()
