# function to display menu
def menu_print():
    print('            Vending Machine              \n')
    print('                 Chips                   \n')
    print('Item             Price               Code\n')
    print('Doritos          5 AED                A1   ')
    print('Cheetos          5 AED                A2   ')
    print('Pringles         5 AED                A3   ')
    print('Stix             5 AED                A4   ')
    print('Lays             5 AED                A5 \n')
    print('                 Drinks                  \n')
    print('Item             Price               Code\n')
    print('Pepsi            3 AED                B6   ')
    print('Mountain Dew     3 AED                B7   ')
    print('Fanta            3 AED                B8   ')
    print('Bottled Water    2 AED                B9   ')
    print('Iced Coffee      5 AED                B10  ')


def vend_machine():

    # menu storage
    menu = [
        {'item' : 'Doritos', 'code': 'A1', 'price' : 5,'stock' : 1},
        {'item' : 'Cheetos', 'code': 'A2', 'price' : 5,'stock' : 5},
        {'item' : 'Pringles', 'code': 'A3', 'price' : 5,'stock' : 2},
        {'item' : 'Stix', 'code': 'A4', 'price' : 5,'stock' : 17},
        {'item' : 'Lays', 'code': 'A5', 'price' : 5,'stock' : 5},
        {'item' : 'Pepsi', 'code': 'B6', 'price' : 3,'stock' : 1},
        {'item' : 'Mountain Dew', 'code': 'B7', 'price' : 3,'stock' : 14},
        {'item' : 'Fanta', 'code': 'B8', 'price' : 3,'stock' : 5},
        {'item' : 'Bottled Water', 'code': 'B9', 'price' : 2,'stock' : 3},
        {'item' : 'Iced Coffee', 'code': 'B10', 'price' : 5,'stock' : 10},
    ]

    # show menu display
    menu_print()


    vend_cash = 1000
    user_cash = int(input('\nEnter Amount in AED: '))

    while True:
        user_input = input('\nEnter Code: ')
        user = user_input.capitalize()
        
        for item in menu:
            if user == item['code']:
                user = item
                price = item['price']
                stock = item['stock']
                vend_cash -= price

                if vend_cash >= price:
                    if stock == 0:
                        print('\nItem Out of Stock')
                        cont = input('\nContinue buying?(yes/no)\n')
                        if cont == 'no':
                            print('\nAED', user_cash, 'has been refunded. Thank you! Have a nice day!')
                            return
                        else:
                            continue
        
                    while user_cash < price:
                        user_cash = int(input('\nInsufficient Amount.\n\nEnter 0 to Exit Vending Machine or Insert ' + str(price - user_cash) + ' AED: '))
                        if user_cash == 0:
                            print('\nThank you! Have a nice day.')
                            return
                        else:
                            continue

                    else:
                        print('\nOne', user['item'], 'has been dispensed.')
                        user['stock'] -= 1
                        user_cash -= price

                        buy_more = input('\nBuy more?(yes/no)\n')
                        if buy_more == 'yes':
                            continue
                        else:
                            if user_cash != 0:
                                print('\nAED', str(user_cash), 'has been refunded.')
                                print('Thank you! Have a nice day!')
                                return
                            else:
                                print('\nThank you! Have a nice day!')
                                return
                else:                    
                    print('\nMachine Out of Change.')
                    print('AED', user_cash, 'has been refunded')
                    print('Thank you! Have a nice day!')
                    return

vend_machine()