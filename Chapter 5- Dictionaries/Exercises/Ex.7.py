personal_info = {"Name" : "Sam", "Age" : 19, "Nationality" : "Filipino", "Gender" : "Female"}

print('Personal Information:')
for keys, values in personal_info.items():
    print("\t", keys, ":", values)

personal_info.update({"Blood Type" : "O+"})

personal_info["Age"] = 20

print("\nUpdated Personal Information:")
for keys, values in personal_info.items():
    print("\t", keys, ":", values)