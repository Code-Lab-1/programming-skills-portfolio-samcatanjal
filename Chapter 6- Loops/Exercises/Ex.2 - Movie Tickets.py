from cmd import PROMPT


PROMPT = "What is your age?\n"

while True:
    age = input(PROMPT)
    if age < 3:
        print("The ticket is free\n")
    elif age < 12:
        print("The ticket is $10\n")
    else:
        print("The ticket is $15\n")