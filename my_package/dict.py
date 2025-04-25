#dict as key value pair
print("====dict====")
my_dict = {
    "name": "Sai",
    "age": 35,
    "location": "Chennai"}
for key, value in my_dict.items():
    print(key, "→", value)

student = {
    "name": "Vishwa",
    "grade": "5th",
    "marks": [85, 90, 88]}
print(student["marks"])       
student["passed"] = True    

my_dict.get("name")           
my_dict.pop("age")           
my_dict.clear()  


