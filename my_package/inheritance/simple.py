#simple
class Parent:
    # Base class
    def display(self):
        print("This is the parent class.")

class Child(Parent):
    # Derived class
    def show(self):
        print("This is the child class.")

# Usage
obj = Child()
obj.display() 
obj.show()     
