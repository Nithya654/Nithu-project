class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        self.total = 0
        self.grade = ""

    def calculate_total(self):
        self.total = sum(self.marks)

    def calculate_grade(self):
        if self.total >= 270:
            self.grade = "A"
        elif self.total >= 240:
            self.grade = "B"
        elif self.total >= 200:
            self.grade = "C"
        else:
            self.grade = "D"

    def display_info(self):
        print("Student Information")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll}")
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {self.total}")
        print(f"Grade: {self.grade}")

student1 = Student("Nithya", "1", [85, 90, 88])
student1.calculate_total()
student1.calculate_grade()
student1.display_info()

student2 = Student("Pavi", "2", [78, 82, 80])
student2.calculate_total()
student2.calculate_grade()
student2.display_info()
