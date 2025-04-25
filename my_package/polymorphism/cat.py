
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

#same function for different object types
dog = Dog()
cat = Cat()

animal_sound(dog)  
animal_sound(cat)  
