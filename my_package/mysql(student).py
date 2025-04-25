import csv
import mysql.connector

# MySQL Connection Config
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nithya",  
    database="testdb"
)
cursor = conn.cursor()

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")

    # Save to CSV
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age])

    # Insert into DB
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    print("Student added successfully.\n")

def view_students_from_file():
    print("\nStudents from CSV:")
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def view_students_from_db():
    print("\nStudents from DB:")
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def update_student():
    student_id = input("Enter ID of student to update: ")
    new_age = input("Enter new age: ")
    cursor.execute("UPDATE students SET age=%s WHERE id=%s", (new_age, student_id))
    conn.commit()
    print("Student updated.\n")

def delete_student():
    student_id = input("Enter ID of student to delete: ")
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    print("Student deleted.\n")

def export_to_new_csv():
    cursor.execute("SELECT name, age FROM students")
    rows = cursor.fetchall()
    with open('exported_students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age'])
        writer.writerows(rows)
    print("Data exported to exported_students.csv\n")

# Menu
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. View Students from File")
    print("3. View Students from DB")
    print("4. Update Student in DB")
    print("5. Delete Student from DB")
    print("6. Export DB Records to CSV")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students_from_file()
    elif choice == '3':
        view_students_from_db()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        export_to_new_csv()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Try again.")

# Close DB connection
cursor.close()
conn.close()
