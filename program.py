import sys
import json


def combo_lookup(menu, target):
    menu = list(menu.items())
    for i in range(len(menu)):
        names, prices = [], []
        names.append(menu[i][0])
        prices.append(menu[i][1])
        if prices[0] == target:
            print(names[0])
            return
        for j in range(i+1, len(menu)):
            names.append(menu[j][0])
            prices.append(menu[j][1])
            if sum(prices) == target:
                print(names)
                return
    print("There is no combination of dishes that is equal to the target price")


try:
    cli_arg = sys.argv[1]
    file = open(cli_arg, "r")
    obj = json.load(file)
    target_price = obj["target_price"]
    menu = obj["menu"]
    combo_lookup(menu, target_price)
except:
    print('No argument given')
