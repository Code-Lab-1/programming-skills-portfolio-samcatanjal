
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


    vend_cash = 1000 # cash in machine
    user_cash = int(input('\nEnter Amount in AED: ')) # user inputs amount of cash

    while True:
        user_input = input('\nEnter Code: ') # user input code
        user = user_input.capitalize() # here just to ensure all user input(ex. a1 or A1) is accepted
        
        for item in menu: # to get the item dictionries from inside menu list
            if user == item['code']: # runs if user input is found in item codes, else nothing happens and continues
                user = item 
                price = item['price']
                stock = item['stock']
                vend_cash -= price # subtract price(item that user bought) from cash in machine

                if vend_cash >= price: # runs if there is still money in machine, if not it goes to else statement
                    if stock == 0: # runs when item selcted is out of stock, if not it goes to else statement
                        print('\nItem Out of Stock')
                        cont = input('\nContinue buying?(yes/no)\n') # asks user if they want to continue buying
                        if cont == 'no': # runs if they want to exit
                            print('\nAED', user_cash, 'has been refunded. Thank you! Have a nice day!') # refunds remaining amount given (out of stock)
                            return
                        else: # yes, program continues
                            continue
        
                    while user_cash < price: # runs to ask user to input more money if what they put in is insufficient
                        user_cash = int(input('\nInsufficient Amount.\n\nEnter 0 to Exit Vending Machine or Insert ' + str(price - user_cash) + ' AED: ')) #add money or exit by entering 0
                        if user_cash == 0: # stops program
                            print('\nThank you! Have a nice day.')
                            return
                        else: # inputs amount and item is payed. program continues
                            continue

                    else: # runs when item is still in stock
                        print('\nOne', user['item'], 'has been dispensed.') # message to say item is dispensed
                        user['stock'] -= 1 # removes said item from stock
                        user_cash -= price # price of item is subtracted from cash inputted by user

                        buy_more = input('\nBuy more?(yes/no)\n') # asks user if they want to continue or not
                        if buy_more == 'yes': # continues program
                            continue
                        else: # no, runs if user want to exit
                            if user_cash != 0: # if they have remaining balance, this refund message will appear
                                print('\nAED', str(user_cash), 'has been refunded.')
                                print('Thank you! Have a nice day!')
                                return
                            else: # if they had 0 balance left, this appears
                                print('\nThank you! Have a nice day!')
                                return

                else: # runs if there is no more change to give to user                    
                    print('\nMachine Out of Change.')
                    print('AED', user_cash, 'has been refunded')
                    print('Thank you! Have a nice day!')
                    return

vend_machine()