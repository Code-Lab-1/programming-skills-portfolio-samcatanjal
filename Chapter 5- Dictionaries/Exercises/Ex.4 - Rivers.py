rivers = {'Nile' : 'Egypt', 'Murray' : 'New South Wales', 'Amazon' : 'Brazil, Columbia, and Peru'}

for keys, values in rivers.items():
    print('\nThe ' + keys + ' river runs through ' + values + '.')

for keys in rivers.keys():
    print(keys)

for values in rivers.values():
    print(values)