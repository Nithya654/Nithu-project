#create a simple student score manger
students = ("Sai", "Anya", "Vishwa")
marks = [85, 90, 95]

#Mapping student names to marks
student_scores = {
    students[0]: marks[0],
    students[1]: marks[1],
    students[2]: marks[2]
}
unique_scores = set(marks)
print(" Student Scores:")

for name, score in student_scores.items():
    print(f"{name} → {score}")

# Adding new mark and update list and set
new_mark = 90
marks.append(new_mark)
# Set -no duplicate
unique_scores.add(new_mark) 

print("\n Updated Marks List:", marks)
print(" Unique Scores Set:", unique_scores)
print(" Number of Students:", len(students))



