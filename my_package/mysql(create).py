import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nithya",  
    database="db"
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT
)
""")

print("Table created successfully.")
conn.close()

#insert records
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="Nithya", database="db"
)
cursor = conn.cursor()

sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
data = ("Alice", 22)

cursor.execute(sql, data)
conn.commit()
print("Record inserted.")
conn.close()

#read record
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="Nithya", database="db"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()

#update record
conn = mysql.connector.connect(
    host="localhost", user="root", password="Nithya", database="db"
)
cursor = conn.cursor()

sql = "UPDATE students SET age = %s WHERE name = %s"
data = (23, "Alice")

cursor.execute(sql, data)
conn.commit()
print("Record updated.")
conn.close()

#delete record
conn = mysql.connector.connect(
    host="localhost", user="root", password="Nithya", database="db"
)
cursor = conn.cursor()

sql = "DELETE FROM students WHERE name = %s"
data = ("Alice",)

cursor.execute(sql, data)
conn.commit()
print("Record deleted.")
conn.close()

#exception handling
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost", user="root", password="Nithya", database="db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
except mysql.connector.Error as e:
    print("Error:", e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
