sandwich_orders = ['Chicken Sandwich', 'Pastrami', 'Egg Sandwich', 'Pastrami', 'Grilled Cheese', 'Ham Sandwich', 'Pastrami', 'Nutella Sandwich']

finished_sandwiches = []

print('\nThe deli has run out of pastrami.\n')

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

for sandwiches in sandwich_orders:
    print('I am making your ' + sandwiches + '.')
    finished_sandwiches.append(sandwich_orders.pop())

print('\n')
for sandwich in finished_sandwiches:
    print('Your ' + sandwich + ' is ready.')