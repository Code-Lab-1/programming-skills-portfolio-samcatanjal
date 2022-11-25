even = []
odd = []

for i in range(0,100):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers from 0 to 100: ", even)
print("Odd numbers from 0 to 100: ", odd)