students = {
    "1": {"name": "Nithya", "marks": [85, 90, 88, 92], "grade": "", "status": "", "subjects": {"Maths": 85, "Science": 90, "English": 88, "Social": 92}},
    "2": {"name": "Pavithra", "marks": [75, 80, 85, 90], "grade": "", "status": "", "subjects": {"Maths": 75, "Science": 80, "English": 85, "Social": 90}},
    "3": {"name": "Kani", "marks": [65, 70, 80, 75], "grade": "", "status": "", "subjects": {"Maths": 65, "Science": 70, "English": 80, "Social": 75}},
    "4": {"name": "Sakthi", "marks": [95, 88, 93, 90], "grade": "", "status": "", "subjects": {"Maths": 95, "Science": 88, "English": 93, "Social": 90}}
}

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(average):
    if average >= 90: return "A"
    elif average >= 75: return "B"
    elif average >= 50: return "C"
    else: return "D"

def calculate_status(average):
    return "Pass" if average >= 50 else "Fail"

def generate_report_card(student_id):
    student = students[student_id]
    marks = student["marks"]
    total = sum(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    status = calculate_status(average)
    student["grade"] = grade
    student["status"] = status
    print(f"\n--- Report Card for {student['name']} ---")
    print("Subject-wise Marks:")
    for subject in student["subjects"]:
        print(f"{subject}: {student['subjects'][subject]}")
    print(f"\nTotal Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")
    print("-" * 30)

def highest_average_student():
    return max(students.items(), key=lambda x: calculate_average(x[1]["marks"]))

def lowest_average_student():
    return min(students.items(), key=lambda x: calculate_average(x[1]["marks"]))

def main():
    while True:
        print("\n=== Student Marks Report Card System ===")
        print("1. View Report Card")
        print("2. Highest Average Marks")
        print("3. Lowest Average Marks")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            student_id = input("Enter Student ID: ")
            if student_id in students:
                generate_report_card(student_id)
            else:
                print("Invalid Student ID.")
        elif choice == "2":
            top_student = highest_average_student()[1]
            print(f"\nStudent with Highest Average Marks: {top_student['name']}")
            print(f"Average Marks: {calculate_average(top_student['marks']):.2f}")
            
        elif choice == "3":
            bottom_student = lowest_average_student()[1]
            print(f"\nStudent with Lowest Average Marks: {bottom_student['name']}")
            print(f"Average Marks: {calculate_average(bottom_student['marks']):.2f}")
           
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

main()
