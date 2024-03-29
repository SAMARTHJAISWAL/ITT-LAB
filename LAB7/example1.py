import sqlite3

conn=sqlite3.connect('test.db')
print("opened database")

cur = conn.cursor()

cur.execute('''
CREATE TABLE COMPAN
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);
'''
            )
print("created")

cur.execute("INSERT INTO COMPAN VALUES (1,'Samarth',19,'Purnia',20000.0)")
cur.execute("INSERT INTO COMPAN VALUES (2,'Triya',21,'Ranchi',15000.0)")
cur.execute("INSERT INTO COMPAN VALUES (3,'Aryan',22,'Faridabad',20000.0)")
cur.execute("INSERT INTO COMPAN VALUES (4,'Priyanshu',21,'Kanpur',65000.0)")

print("inserted")

cursor = cur.execute("SELECT id, name, address, salary FROM COMPAN")
# Iterate through the result set and print each record
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

# Update the salary for the record with ID=1
cur.execute("UPDATE COMPAN SET SALARY = 25000.00 WHERE ID = 1;")

# Commit the changes to the database
conn.commit()
print("Total number of rows updated:", conn.total_changes)

# Retrieve and print the updated records from the COMPANY table
cursor = cur.execute("SELECT id, name, address, salary FROM COMPAN")
for row in cursor:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("ADDRESS =", row[2])
    print("SALARY =", row[3], "\n")


# Delete the record with ID=2 from the COMPANY table
cur.execute("DELETE FROM COMPAN WHERE ID = 2;")

# Commit the changes to the database
conn.commit()
print("Total number of rows deleted:", conn.total_changes)

# Retrieve and print the remaining records from the COMPANY table
cursor = cur.execute("SELECT id, name, address, salary FROM COMPAN")
for row in cursor:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("ADDRESS =", row[2])
    print("SALARY =", row[3], "\n")

print("Operation done successfully")
conn.close()
