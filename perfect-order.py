import sys
import json
import math
from itertools import combinations


def print_menu(menu, array):
    dishes = []
    for i in range(len(array)):
        dishes.append(menu[array[i]])
    print('The dishes you could order that add up to your target price include:')
    print(', '.join(dishes))


def combo_lookup(menu, target):
    prices = list(menu.keys())
    for i in range(1, len(prices) + 1):
        combos = list(combinations(prices, i))
        for j in range(len(combos)):
            if math.fsum(combos[j]) == target:
                return print_menu(menu, combos[j])
    print("There is no combination of dishes that is equal to the target price")


#### Program init ####
try:
    cli_arg = sys.argv[1]
    file = open(cli_arg, "r")
    obj = json.load(file)
    target_price = obj["target_price"]
    menu = {}
    for dish in obj["menu"]:
        menu[obj["menu"][dish]] = dish
    combo_lookup(menu, target_price)
except:
    print('Please include an argument')
