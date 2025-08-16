days= ("monday","tuesday","wensday","thursday","friday")
activities_for_monday =input("Enter your activity for monday:")
activities_for_tuesday = input("Enter your activity for tuesday:")
activities_for_wensday = input("Enter your activities for wensday: ")
activities= {activities_for_monday,activities_for_tuesday,activities_for_monday}
activities_paring = dict(zip(days, activities))
print(activities_paring)