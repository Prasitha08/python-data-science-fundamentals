"""
Python & Data Science Fundamentals — Beginner Practice
Run: python python_fundamentals.py
"""

# 1. Variables and data types
student_name = "Anu"
student_age = 20
average_score = 86.5
is_enrolled = True

print("1. VARIABLES")
print("Name:", student_name)
print("Age:", student_age)
print("Average score:", average_score)
print("Currently enrolled:", is_enrolled)
print("Data type of score:", type(average_score).__name__)

# 2. Operators
print("\n2. OPERATORS")
first_number = 18
second_number = 4
print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)
print("Remainder:", first_number % second_number)

# 3. Conditional statements
print("\n3. CONDITIONAL STATEMENTS")
mark = 78
if mark >= 90:
    grade = "A"
elif mark >= 75:
    grade = "B"
elif mark >= 50:
    grade = "C"
else:
    grade = "Needs improvement"
print("Mark:", mark, "| Grade:", grade)

# 4. For loop
print("\n4. FOR LOOP")
for day in range(1, 5):
    print("Day", day, "- Practise Python")

# 5. While loop
print("\n5. WHILE LOOP")
count = 1
while count <= 3:
    print("Count:", count)
    count += 1

# 6. Functions
print("\n6. FUNCTIONS")
def calculate_average(values):
    """Return the average of a non-empty list of numbers."""
    if not values:
        return 0
    return sum(values) / len(values)

scores = [80, 75, 90, 85]
print("Scores:", scores)
print("Average:", calculate_average(scores))

# 7. Lists
print("\n7. LISTS")
subjects = ["Python", "Statistics", "Data Science"]
subjects.append("Machine Learning")
for subject in subjects:
    print("-", subject)

# 8. Dictionaries
print("\n8. DICTIONARIES")
student = {
    "name": "Anu",
    "course": "Data Science",
    "completed_days": 4
}
for key, value in student.items():
    print(f"{key}: {value}")

# 9. File handling
print("\n9. FILE HANDLING")
sample_text = "Python makes data analysis easier."
with open("learning_note.txt", "w", encoding="utf-8") as file:
    file.write(sample_text)

with open("learning_note.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("Read from file:", content)

print("\nPractice completed!")
