from audioop import reverse


places = ['The Great Wall of China','The Grand Canyon','Amazon Rainforest','The Colosseum','Machu Picchu']

print('Original order:')
print(places)

print('\nAlphabetical order using sorted():')
print(sorted(places))

print('\n' + places)

print('\nReverse alphabetical order using sorted():')
print(sorted(places, reverse=True))

print('\n' + places)

print('\nChange list order using reverse():')
places.reverse()
print(places)

print('\nChange list order again using reverse():')
places.reverse()
print(places)

print('\nAlphabetical order using sort():')
places.sort()
print(places)

print('\nReverse alphabetical order using sort():')
places.sort(reverse= True)
print(places)