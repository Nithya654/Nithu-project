class Farmer:
    def work(self):
        print("The farmer is working on the field.")

class CropFarmer(Farmer):
    def work(self):
        print("The crop farmer is planting wheat.")

class DairyFarmer(Farmer):
    def work(self):
        print("The dairy farmer is milking cows.")

# List of farmers
farmers = [CropFarmer(), DairyFarmer()]

for f in farmers:
    f.work()  # Calls work()
