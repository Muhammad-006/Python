# TODO 1. Print REPORT.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 3. Process Coins.
def process_coins(price):
    print('Please insert coins: ')
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickels = int(input('How many nickels? '))
    pennies = int(input('How many pennies? '))
    sum = quarters/4 + dimes/10 + nickels/20 + pennies/100
    sum = round(sum, 2)
    print("You provided:", sum)
    # TODO 4. Check transaction successful.
    if price < sum:
        sum -= price
        sum = round(sum, 2)
        print (f'Here is your change {sum}. 🤑')
        return True
    elif price == sum:
        print('Your transaction is successful. 🤑')
        return True
    else:
        print('Sorry! Your given price is not sufficient.\nAmount refunded. 🤬')
        return False


money = 0
check = True

while check == True:
    print('\n\n')
    choice = input("What do you want?('espresso', 'latte', 'cappuccino', 'report'): ").lower()
    if choice == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: {money}")
# TODO 2. Check sufficient resources.
    elif choice == 'espresso':
        temp_water = MENU[choice]['ingredients']['water']
        temp_coffee = MENU[choice]['ingredients']['coffee']
        cost = MENU[choice]['cost']
        if temp_water > resources['water'] or temp_coffee > resources['coffee']:
            print('Sorry! we ran out of resources. 😭😭😭')
            check = False
        else:
            maker = process_coins(price = cost)
            if maker:
                resources['water'] -= temp_water
                resources['coffee'] -= temp_coffee
                print(f"Here is your {choice}.\tEnjoy! ☕")
                money += cost

    elif choice == 'latte' or choice == 'cappuccino':
        temp_water = MENU[choice]['ingredients']['water']
        temp_coffee = MENU[choice]['ingredients']['coffee']
        temp_milk = MENU[choice]['ingredients']['milk']
        cost = MENU[choice]['cost']
        if temp_water > resources['water'] or temp_coffee > resources['coffee'] or temp_milk > resources['milk']:
            print('Sorry! we ran out of resources. 😭😭😭')
            espresso_water = MENU['espresso']['ingredients']['water']
            espresso_coffee = MENU['espresso']['ingredients']['coffee']
            if espresso_water > resources['water'] or espresso_coffee > resources['coffee']:
                check = False
        else:
            maker = process_coins(price = cost)
            if maker:
                resources['water'] -= temp_water
                resources['coffee'] -= temp_coffee
                resources['milk'] -= temp_milk
                print(f"Here is your {choice}.\tEnjoy! ☕")
                money += cost
    else:
        print('Sorry! Wrong choice.')

# TODO 4. Check transaction successful.
# TODO 5. Make coffee. ☕