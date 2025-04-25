import json
import xml.etree.ElementTree as ET
import openpyxl

# static student data stored in a list of dictionaries
students = [
    {"name": "Nithya", "roll": "1", "marks": [85, 78, 92]},
    {"name": "Pavi", "roll": "2", "marks": [56, 65, 60]},
    {"name": "Kani", "roll": "3", "marks": [95, 98, 97]}
]

# calculate total marks and grade
def calculate_total_and_grade():
    for student in students:
        marks = student["marks"]
        total = sum(marks)
        avg = total / len(marks)

        if avg >= 90:
            grade = 'A'
        elif avg >= 75:
            grade = 'B'
        elif avg >= 60:
            grade = 'C'
        elif avg >= 40:
            grade = 'D'
        else:
            grade = 'F'

        student["total"] = total
        student["grade"] = grade

# display student details
def display_students():
    for s in students:
        print("\nName:", s["name"])
        print("Roll No:", s["roll"])
        print("Marks:", s["marks"])
        print("Total:", s["total"])
        print("Grade:", s["grade"])

# save to JSON file
def save_to_json():
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)
    print("\nData saved to JSON.")

# save to XML file
def save_to_xml():
    root = ET.Element("Students")
    for s in students:
        student = ET.SubElement(root, "Student")
        ET.SubElement(student, "Name").text = s["name"]
        ET.SubElement(student, "Roll").text = s["roll"]
        ET.SubElement(student, "Marks").text = str(s["marks"])
        ET.SubElement(student, "Total").text = str(s["total"])
        ET.SubElement(student, "Grade").text = s["grade"]

    tree = ET.ElementTree(root)
    tree.write("students.xml")
    print("Data saved to XML.")

# save to Excel file
def save_to_excel():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["Name", "Roll", "Marks", "Total", "Grade"])

    for s in students:
        sheet.append([s["name"], s["roll"], str(s["marks"]), s["total"], s["grade"]])

    wb.save("students.xlsx")
    print("Data saved to Excel.")

# main function to run everything
def main():
    calculate_total_and_grade()
    display_students()
    save_to_json()
    save_to_xml()
    save_to_excel()

main()
