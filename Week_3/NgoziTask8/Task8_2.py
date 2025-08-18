# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")
''' The  code is confirming the eligilibity of a candidate to be enrroled in a program but from the output the candidate is not eligible'''

# Working on the case
# name = input("Enter your Name :")
citizenship = input("What is your Citizenship status")
Enrollment= input("Are you enrolled in a well known Nigerian Unversity(YES/NO):")
other_scholarship = input("Are You a reciepent of any other scholarship under the Oil and gas Industry (YES/NO): ")
Academic_qualification = input("Do you have five distinctions ")
eligibility = ((citizenship == "Nigeria") or citizenship == "Nigerian")and (Enrollment == "YES") and (other_scholarship == "NO") and (Academic_qualification == "YES")

print(f"Citizenship: {citizenship}\nEnrollment: {Enrollment}\n Are You Holding any other Oil& gas scholarship: {other_scholarship}\n Do you have five distinctions : {Academic_qualification}\nEligible: {eligibility}")