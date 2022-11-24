sandwich_orders = ['Chicken Sandwich', 'Egg Sandwich', 'Grilled Cheese', 'Ham Sandwich', 'Nutella Sandwich']

finished_sandwiches = []

for sandwiches in sandwich_orders:
    print('I am making your ' + sandwiches + '.')
    finished_sandwiches.append(sandwich_orders.pop())

print('\n')
for sandwich in finished_sandwiches:
    print('Your ' + sandwich + ' is ready.')