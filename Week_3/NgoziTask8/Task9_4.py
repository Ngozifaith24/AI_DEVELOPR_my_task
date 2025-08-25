# **Task6: Attendance Tracker**
# - Write a Python program that;

#  - Stores the days of the week in a tuple.

#  - Stores the months of the year in another tuple.

#  - Asks the user to enter:

#    - Student’s name

#    - Gender

#    - Course Track
   
#    - Current month number (1-12)

#    - Current day number (1-7)
days_of_the_week = ("Monday", "Tuesday", "Wensday", "Thursday", "Friday", "Saturday", "Sunday")
Mnths_of_d_year = ("Jan", "feb", "March", "....")
while True:
    student_input = input("enter your name: ")
    student_input_gender = input("Enter your gender:").lower()
    student_input_course = input("Enter your gender:").lower()
    student_input_month = int(input("Enter your gender:"))
    student_input_day = int(input("Enter your gender:"))
    if student_input_day == "Monday":
        print("Invalid entry.... try again")
        break
    else:
        print("Confirmed")

