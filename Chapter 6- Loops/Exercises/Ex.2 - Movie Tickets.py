from cmd import PROMPT


PROMPT = 'Input your age: '

while True:
    age = input(PROMPT)

    if age == 'finished':
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
