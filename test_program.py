from perfect_order import combo_lookup, print_menu

eg_menu = {
    7.00: "appetizer",
    3.00: "drink",
    13.00: "entree_1",
    11.00: "entree_2",
    15.00: "entree_3"
}
no_combo_menu = {
    7.00: "appetizer",
    3.00: "drink",
    13.00: "entree_1",
    11.00: "entree_2",
    16.00: "entree_3"
}

prices = (7.00, 3.00, 15.00)


def test_correct_combo():
    assert combo_lookup(eg_menu, 25.00) == (7.00, 3.00, 15.00)


def test_correct_combo_with_no_perfect_order():
    assert combo_lookup(no_combo_menu, 25.00) == None


def test_correct_dishes():
    assert print_menu(eg_menu, prices) == "appetizer, drink, entree_3"
