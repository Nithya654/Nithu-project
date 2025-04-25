class Employee:
    def __init__(self, name, base_salary):#--constructor
        self.name = name
        self.__base_salary = base_salary # base_salary is encapsulation

    def calculate_salary(self):
        return self.__base_salary
    
# Inheritance
class Developer(Employee):
    def calculate_salary(self):
        return super().calculate_salary() + 2000

class Manager(Employee):
    def calculate_salary(self):
        return super().calculate_salary() + 5000

#polymorphism–
employees = [Developer("Nithya", 30000), Manager("Divya", 40000)]

for emp in employees:
    print(f"{emp.name}'s Salary: ₹{emp.calculate_salary()}")



