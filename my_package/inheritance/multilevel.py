#multi level 
class Person:
    def info(self):
        print("I am a person.")

class Employee(Person):
    def job(self):
        print("I am an employee.")

class Manager(Employee):
    def role(self):
        print("I manage a team.")

print("Multi level inheritance")
m = Manager()
m.info()
m.job()
m.role()

