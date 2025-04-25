import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nithya",  # <- use new password here
    database="db"       # <- make sure this DB exists!
)

if conn.is_connected():
    print("✅ Connected to MySQL")

conn.close()


