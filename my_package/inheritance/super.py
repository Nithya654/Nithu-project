# super-Use super() to call base class methods.

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Call parent method
        print("Hello from Child")

obj = Child()
obj.greet()
