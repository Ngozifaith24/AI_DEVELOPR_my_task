student = {}
name = input("Enter your Name: ")
age = int(input("Enter Your age: "))
student["Sudent Name"]=name
student["Student age"]= age
lst_of_score = [70,67,60]
student["Student Score"]= lst_of_score
average_score = sum(lst_of_score)/ len(lst_of_score)
passed = average_score>=50
student ["Passed"] =passed
teenger = age >=13 and age<=19
student["Teenger"]= teenger
print(f"NAME:{student['Sudent Name']}\nAGE: {student['Student age']}\nScores:{student['Student Score']}\nPassed{student['Passed']}\nTeenager:{student['Teenger']}")
