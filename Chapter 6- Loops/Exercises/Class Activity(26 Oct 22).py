#Class Activity 1

words = ['Apple','Banana','Car','Dolphin']

for x in words:
    print("The following lines will print each letter of ", x)
    for letters in x:
        print(letters)


# Class Activity 2

numbers = [2,4,6,8,10,12]
sum = 0
for x in numbers:
    sum = sum + x
    print("The sum is", sum)


# CLass Activity 3

shoe_brands = ['adidas','nike','skechers']

for x in range(len(shoe_brands)):
    print("I like", shoe_brands[x])


# Class Activity 4

num = [1,12,32,7,108,9,10,5,25]

for x in num:
    print(x)
else:
    print("No items left.")