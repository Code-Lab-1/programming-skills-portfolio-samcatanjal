even = []
odd = []

for i in range(0,100):
    if i % 2 == 0:
        even.append(i)
        if i == 50:
            break
    else:
        odd.append(i)
        if i == 50:
            break

print("Even numbers until: ", even)
print("Odd numbers until: ", odd)
