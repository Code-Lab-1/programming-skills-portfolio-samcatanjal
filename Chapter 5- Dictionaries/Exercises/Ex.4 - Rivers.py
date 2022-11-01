rivers = {'Nile' : 'Egypt', 'Amazon' : 'Brazil, Peru, and Columbia', 'Thames' : 'London'}

for river, country in rivers.items():
    print('\nThe ' + river + ' river runs through ' + country + '.')

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)