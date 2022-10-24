places = ['The Great Wall of China','The Grand Canyon','Amazon Rainforest','The Colosseum','Machu Picchu']

print('Original order:')
print(places)

print('\nAlphabetical order using sorted():')
print(sorted(places))

print('\nOriginal order:')
print(places)

print('\nReverse alphabetical order using sorted():')
print(sorted(places, reverse=True))

print('\nOriginal order:')
print(places)

print('\nReverse alphabetical order using reverse():')
places.reverse()
print(places)

print('\nReverse alphabetical order using sort():')
places.sort()
print(places)