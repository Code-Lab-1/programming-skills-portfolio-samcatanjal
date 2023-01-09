from cmd import PROMPT


PROMPT = "Please enter your pizza toppings.\nEnter the word 'finished' when you are done.\n"

while True:
    pizza_toppings = input(PROMPT)
    if pizza_toppings != 'finished':
        print("\n" + pizza_toppings + " is/are added to your pizza.\n")
    else:
        break