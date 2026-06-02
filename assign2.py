# Input student name
name = input("Enter student name: ")
# Input marks for five subjects
math = (input("Enter marks for math: "))
english = (input("Enter marks for english: "))
kiswahili = (input("Enter marks for kiswahili: "))
science = (input("Enter marks for science: "))
religion = (input("Enter marks for religion: "))

# Store marks in a list
marks = [math, english, kiswahili, science, religion]

subjects = ["Math", "English", "Kiswahili", "Science", "Religion"]

#calculate grade
def get_grade(mark):

    if mark >= 70 and mark <= 79:
        print("A")

    elif mark >= 60 and mark <= 69:
        print("B")

    elif mark >= 50 and mark <= 59:
        print("C")

    elif mark >= 40 and mark <= 49:
        print("D")

    elif mark >= 1 and mark <= 39:
        print("FAIL")

    else:
        print("Invalid")

# Calculate total and average
total = sum(marks)
average = total / 5

# Find minimum mark
mingrade = min(marks)

# Display result
print("\n===== STUDENT RESULT =====")
print("Student Name:", name)

for i in range(len(marks)):
    print(subjects[i], ":", marks[i], "Grade:", end=" ")
    get_grade(marks[i])

print("--------------------------------------")
print("Total Marks:", total)
print("Average Marks:", average)
print("minimum marks",minimum)
