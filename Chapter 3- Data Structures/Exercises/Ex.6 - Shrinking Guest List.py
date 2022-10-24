from unicodedata import name


guests = ['Billie','Kathryn','Margot','Hailee']

print(guests[0] + ", Let's have dinner!")
print(guests[1] +", Let's have dinner!")
print(guests[2] + ", Let's have dinner!")
print(guests[3] + ", Let's have dinner!")

print("\n" + guests[0], "can't make it.")

del(guests[0])
guests.insert(0, "Scarlett")

print("\n" + guests[0] + ", Dinner?")
print(guests[1] +", Dinner?")
print(guests[2] + ", Dinner?")
print(guests[3] + ", Dinner?")

print("\nWe can only invite two people for dinner.")

name = guests.pop()
print("\nSorry, " + name + " we can't invite anymore people.")

name = guests.pop()
print("\nSorry, " + name + " we can't invite anymore people.")

print("\n" + guests[0] + ", you are still invited to dinner. Please Come!")
print(guests[1] +", you are still invited to dinner. Please Come!")

del(guests[0])
del(guests[0])

print(guests)