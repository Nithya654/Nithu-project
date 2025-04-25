# Base class
class Farmer:
    def __init__(self, name, age, village):
        self.name = name
        self.age = age
        self.village = village

    def display_info(self):
        print(f"Farmer Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Village: {self.village}")

# Derived class 1
class CropFarmer(Farmer):
    def grow_crops(self):
        print(f"{self.name} is growing wheat and rice.")

# Derived class 2
class DairyFarmer(Farmer):
    def milk_cows(self):
        print(f"{self.name} is milking 10 cows.")

# Object of CropFarmer
crop_farmer = CropFarmer("guru", 40, "Tenkasi")
crop_farmer.display_info()
crop_farmer.grow_crops()

print()

# Object of DairyFarmer
dairy_farmer = DairyFarmer("Kamal", 50, "thiruvallur")
dairy_farmer.display_info()
dairy_farmer.milk_cows()
