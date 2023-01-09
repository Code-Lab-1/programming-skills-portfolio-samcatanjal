pets = []

animal = {'Name' : 'Max', 'Type' : 'Dog', 'Gender' : 'Male', 'Owner' : 'Sam'}
pets.append(animal)

animal = {'Name' : 'Tiger', 'Type' : 'Cat', 'Gender' : 'Male', 'Owner' : 'Joy'}
pets.append(animal)

animal = {'Name' : 'Biscuit', 'Type' : 'Hamster', 'Gender' : 'Female', 'Owner' : 'Myle'}
pets.append(animal)

for animal in pets:
    print('\nInformation about ' + animal['Name'] + ':')
    for key, value in animal.items():
        print(key + ':' + value)