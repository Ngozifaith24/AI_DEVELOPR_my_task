student_details = {}
details = ["name", "age", "gender", "courses"]

for detail in details:
    value = input(f"Enter your {detail}: ")
    student_details[detail] = value

# Convert courses into a list (comma-separated input)
student_details["courses"] = student_details["courses"].split(',')

# Displaying the details 
print("\nStudent Information:")
print(f"Name: \t\t{student_details['name']}")
print(f"Age: \t\t{student_details['age']}")
print(f"Gender: \t{student_details['gender']}")
print(f"Courses: \t{student_details['courses']}")