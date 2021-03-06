import sys
import json
import math
from itertools import combinations

# Receives array from combo_lookup and finds the respective dishes and prints to console
def print_menu(menu, array):
    dishes = []
    for i in range(len(array)):
        dishes.append(menu[array[i]])
    results = ', '.join(dishes)
    print(f'The dishes you could order that add up to your target price include: \n{results}')
    return results

# Receives menu prices, runs possible combinations and checks for one that adds up to correct price
def combo_lookup(menu, target):
    prices = list(menu.keys())
    for i in range(1, len(prices) + 1):
        combos = list(combinations(prices, i))
        for j in range(len(combos)):
            if math.fsum(combos[j]) == target:
                print_menu(menu, combos[j])
                return combos[j]
    print("There is no combination of dishes that is equal to the target price")


#### Program init ####
# Parse data, return message if error
try:
    cli_arg = sys.argv[1]
    file = open(cli_arg, "r")
    obj = json.load(file)
    target_price = float(obj["target_price"])
    menu = {}
    for dish in obj["menu"]:
        menu[float(obj["menu"][dish])] = dish
    combo_lookup(menu, target_price)
except:
    print('''Please include one argument. If you have included one, please ensure 
it is a properly json-formatted document following the correct menu format''')
