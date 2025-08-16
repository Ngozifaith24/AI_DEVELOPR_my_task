names =("Ngozi","Faith", "Nkech")
nums = ("08137899155", "09044970160","08085547884")
quick_contacts = dict(zip(names,nums))
name = input("Enter a name")
number = quick_contacts.get(names)
if number:
    print(f"{names}'s number is {number}")
else:
    print("Name not found.")