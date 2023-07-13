import data

def calculation(q, i, n, p):
    quarters = 0.25 * q
    dimes = 0.1 * i
    nickles = 0.05 * n
    pennies = 0.01 * p
    total = quarters + dimes + nickles + pennies
    return round(total, 2)


def report(a, b, c, d):
    print(f"Water: {a}ml")
    print(f"Milk: {b}ml")
    print(f"Coffee: {c}g")
    print(f"Money: ${d}")



water = data.resources["water"]
milk = data.resources["milk"]
coffee = data.resources["coffee"]
money = 0

richard = True

while richard:

    select = input("What would you like? (espresso/latte/cappuccino): ")
    if select == "report":
        report(water, milk, coffee, money)

    elif (select == 'espresso'):
        if (water >= data.MENU["espresso"]["ingredients"]["water"]) and (
                coffee >= data.MENU["espresso"]["ingredients"]["coffee"]):
            print("Please insert coins.")
            q1 = int(input("How many quarters?: "))
            d1 = int(input("How many dimes?: "))
            n1 = int(input("How many nickles?: "))
            p1 = int(input("How many pennies?: "))
            ret = calculation(q1, d1, n1, p1)
            real_value = data.MENU["espresso"]["cost"]
            if (ret < real_value):
                print(f"Sorry that's not enough money. ${ret} money refunded.")
                
            elif (ret > real_value):
                h = (ret) - (real_value)
                print(f"Here is ${h} in change.")
                print("Here is your espresso ☕ Enjoy!")
                money = money + real_value
                water = water - (data.MENU["espresso"]["ingredients"]["water"])
                coffee = coffee - (data.MENU["espresso"]["ingredients"]["coffee"])
                
        elif water < data.MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            
        elif coffee < data.MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is no coffee.")
            


    elif (select == 'latte'):
        if (water >= data.MENU["latte"]["ingredients"]["water"]) and (
                coffee >= data.MENU["latte"]["ingredients"]["coffee"]) and (
                milk >= data.MENU["latte"]["ingredients"]["milk"]):
            print("Please insert coins.")
            q1 = int(input("How many quarters?: "))
            d1 = int(input("How many dimes?: "))
            n1 = int(input("How many nickles?: "))
            p1 = int(input("How many pennies?: "))
            ret = calculation(q1, d1, n1, p1)
            real_value = data.MENU["latte"]["cost"]
            if (ret < real_value):
                print(f"Sorry that's not enough money. ${ret} money refunded.")
                
            elif (ret > real_value):
                h = (ret) - (real_value)
                print(f"Here is ${h} in change.")
                print("Here is your latte ☕ Enjoy!")
                money = money + real_value
                water = water - (data.MENU["latte"]["ingredients"]["water"])
                milk= milk - (data.MENU["latte"]["ingredients"]["milk"])
                coffee = coffee - (data.MENU["latte"]["ingredients"]["coffee"])
                
        elif water < data.MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            
        elif coffee < data.MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is no coffee.")
            
        elif milk < data.MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            


    elif (select == 'cappuccino'):
        if (water >= data.MENU["cappuccino"]["ingredients"]["water"]) and (
                coffee >= data.MENU["cappuccino"]["ingredients"]["coffee"]) and (
                milk >= data.MENU["cappuccino"]["ingredients"]["milk"]):
            print("Please insert coins.")
            q1 = int(input("How many quarters?: "))
            d1 = int(input("How many dimes?: "))
            n1 = int(input("How many nickles?: "))
            p1 = int(input("How many pennies?: "))
            ret = calculation(q1, d1, n1, p1)
            real_value = data.MENU["cappuccino"]["cost"]
            if (ret < real_value):
                print(f"Sorry that's not enough money. ${ret} money refunded.")
                
            elif (ret > real_value):
                h = (ret) - (real_value)
                print(f"Here is ${h} in change.")
                print("Here is your cappuccino ☕ Enjoy!")
                money = money + real_value
                water = water - (data.MENU["cappuccino"]["ingredients"]["water"])
                milk = milk - (data.MENU["cappuccino"]["ingredients"]["milk"])
                coffee = coffee - (data.MENU["cappuccino"]["ingredients"]["coffee"])
                
        elif water < data.MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            
        elif coffee < data.MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is no coffee.")
            
        elif milk < data.MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
    elif(select=='off'):
        richard=False
            
