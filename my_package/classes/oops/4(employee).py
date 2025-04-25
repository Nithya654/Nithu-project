class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_salary(self):
        print("\nEmployee Salary Details")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))

emp1 = Employee(name, emp_id, salary)
emp1.display_salary()
