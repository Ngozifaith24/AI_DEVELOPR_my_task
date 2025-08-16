#Paitent Profile Builder
# Basic info
name = input("Enter paitent's full name: ")
age = int(input("Enter paitent's age: "))
gender = input("Enter gender(Male/Female):")

#Test prices (3 tests)
tests = ("MP","Widal", "PCV")
prices = tuple(float(input(f"Enter price for {tst}:")) for tst in tests)

#symptoms - Ensuring the symptoms are unique hence the need to use set
symptoms = input("Enter the symptoms you feel(comma-seperated): ")
symptoms_set =set(s.strip() for s in symptoms.split(","))

# Next of kin Info
Next_of_kin_name = input("Enter next of kin's name: ")
Next_of_kin_num = input ("Enter Next of kin's num: ")

#paitent Dictionary
patient_profile = {
    "Basic Info": {
    "Name": name.title(),
    "Age": age,
    "Gender": gender.capitalize()
    },
    "Tests": {tst: price for tst, price in zip(tests, prices)},
    "Next of Kin": {
        "Name": Next_of_kin_name.title(),
        "Phone": Next_of_kin_num
    },
    "Symptoms": list(symptoms_set)
}

#Derived Data
patient_profile["Tests"]["Prices"] = sum(prices) / len(prices)
patient_profile["Basic Info"]["Initial"] ="".join([n[0] for n in name.split()])
patient_profile["Symptoms count"] = len(symptoms_set)

#Output Section
print("\n\t=== PAITENT PROFILE ===")
print(f"Name:\t\t{patient_profile['Basic Info']['Name']}")
print(f"Age:\t\t{patient_profile['Basic Info']['Age']}")
print(f"Gender:\t\t{patient_profile['Basic Info']['Gender']}")
print(f"Initial:\t\t{patient_profile['Basic Info']['Initial']}")
print("\n===Test Prices===")
print(patient_profile["Tests"])
print("\n===Next of kin Info===")
print(patient_profile["Next of Kin"])
print("\n===Symptoms===")
print(patient_profile["Symptoms"])
print(f"\nTotal Symptoms:\t{patient_profile['Symptoms count']}")
print(f"Average price:\t{patient_profile['Tests price average']:.2f}")